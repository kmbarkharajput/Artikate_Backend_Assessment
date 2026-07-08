import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artikate.settings')
app = Celery('artikate')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Utility task for verifying the worker is running. Call with: debug_task.delay()"""
    print(f'Request: {self.request!r}')
