from django.test import TestCase
from jobs.models import EmailJob


class EmailJobTests(TestCase):
    def test_create_email_job(self):
        job = EmailJob.objects.create(
            recipient="test@example.com",
            subject="Assessment",
            body="Hello"
        )

        self.assertEqual(job.status, "PENDING")
        self.assertEqual(job.retry_count, 0)

    def test_string_representation(self):
        job = EmailJob.objects.create(
            recipient="abc@test.com",
            subject="Hi",
            body="Testing"
        )

        self.assertEqual(str(job), "abc@test.com")