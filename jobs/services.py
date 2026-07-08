class EmailService:

    @staticmethod
    def send_email(recipient, subject, body):
        print("Email sent")
        print(recipient)

        return True