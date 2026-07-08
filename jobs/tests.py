from django.test import TestCase
from .models import EmailJob


class EmailJobTests(TestCase):
    def test_job_created(self):
        job = EmailJob.objects.create(
            recipient="test@example.com",
            subject="Hello",
            body="Assessment",
        )

        self.assertEqual(job.status, "PENDING")