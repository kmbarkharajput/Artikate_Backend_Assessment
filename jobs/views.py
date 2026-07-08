from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_email_task


class SendEmailView(APIView):
    def post(self, request):
        recipient = request.data.get("recipient")
        subject = request.data.get("subject")
        body = request.data.get("body")

        send_email_task.delay(
            recipient,
            subject,
            body,
        )

        return Response({
            "message": "Email queued successfully."
        })