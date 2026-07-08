from celery import shared_task


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
    acks_late=True,
)
def send_email_task(self, recipient, subject, body):
    print("Sending email...")
    print(recipient)
    print(subject)


    return True