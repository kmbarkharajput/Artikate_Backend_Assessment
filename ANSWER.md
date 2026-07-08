# ARTIKATE Backend Assessment

# ANSWER.md

## Section 04 – Written Architecture Review

---

# Question A — Django Admin Performance

When a Django Admin page becomes slow with more than 500,000 records, adding an index on the primary key alone is not enough. I would investigate the following three root causes.

## 1. N+1 Database Queries

If the admin list page displays related models through `ForeignKey` or `OneToOneField`, Django executes additional SQL queries for every row, causing poor performance.

### Fix

Use Django Admin's `list_select_related` to automatically perform SQL joins.

```python
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "tenant", "total_amount")
    list_select_related = ("customer", "tenant")
```

For ManyToMany relationships, use `prefetch_related()` inside `get_queryset()`.

```python
def get_queryset(self, request):
    return super().get_queryset(request).prefetch_related("tags")
```

This removes unnecessary database queries and improves page load speed.

---

## 2. Slow Search Queries

Large tables become slow when using:

```python
search_fields = ("customer__name",)
```

because Django generates SQL using `LIKE '%keyword%'`, which often cannot use indexes efficiently.

### Fix

- Search indexed columns.
- Add `db_index=True` where appropriate.
- Use `Meta.indexes`.
- Override `get_search_results()` for custom optimized searching.

Example:

```python
class Customer(models.Model):
    email = models.EmailField(db_index=True)
```

---

## 3. Expensive COUNT Query

The Django admin paginator executes:

```sql
SELECT COUNT(*) FROM orders_order;
```

before displaying every page.

On very large tables this query becomes expensive.

### Fix

Disable the full result count.

```python
class OrderAdmin(admin.ModelAdmin):
    show_full_result_count = False
```

or use a custom paginator.

```python
from django.core.paginator import Paginator
from django.utils.functional import cached_property

class LargeTablePaginator(Paginator):

    @cached_property
    def count(self):
        return 1000000
```

```python
class OrderAdmin(admin.ModelAdmin):
    paginator = LargeTablePaginator
```

This avoids expensive count queries and significantly improves admin performance.

---

# Question B — Pagination Trade-offs

Returning 10,000 records in a single API response increases response time, memory usage, and bandwidth. Django REST Framework provides multiple pagination strategies, with Offset Pagination and Cursor Pagination being the most common.

## Offset Pagination

Example

```
GET /api/orders/?page=5
```

Implemented using:

- `PageNumberPagination`
- `LimitOffsetPagination`

### Advantages

- Very easy to implement.
- Users can jump directly to any page.
- Works well for dashboards and reports.

### Disadvantages

The SQL query uses OFFSET.

Example:

```sql
SELECT * FROM orders_order
LIMIT 20 OFFSET 50000;
```

The database must skip thousands of rows before returning results.

If new rows are inserted or deleted while users paginate, duplicate or missing records may appear.

Performance becomes worse as the offset increases.

---

## Cursor Pagination

Example

```
GET /api/orders/?cursor=eyJvZmZzZXQiOjIw...
```

Implemented using Django REST Framework's `CursorPagination`.

```python
class OrderPagination(CursorPagination):
    ordering = "-created_at"
```

### Advantages

- Uses indexed ordering.
- No large OFFSET scan.
- Stable results while records are inserted or deleted.
- Ideal for infinite scrolling in mobile applications.

### Disadvantages

- Cannot jump directly to page numbers.
- Cursor values are not human-readable.

---

## Which One Would I Choose?

For a mobile application with infinite scrolling, I would choose **CursorPagination** because it scales efficiently, avoids duplicate records during concurrent updates, and performs well on very large datasets.

For an admin dashboard or reporting system where users need direct page navigation, I would choose **Offset Pagination** because page numbers provide a better user experience despite the database cost.

Cursor pagination offers better scalability, while offset pagination offers better usability for traditional interfaces.

---

