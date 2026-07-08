from .models import EmailJob


def move_to_dead_letter(job):
    job.status = "DEAD"
    job.save()