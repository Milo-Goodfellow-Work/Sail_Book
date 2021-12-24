# from listings.models import listing
from sail_book.settings import hidden_settings
from django.core.mail import send_mail
import smtpLib


def send_controls(new_listing):
    try:
        email_body = '''
            We have created your listing!
            If you wish to delete it,
            this can be done at:\n http://127.0.0.1:8000/delete/
        ''' + new_listing.public_token

        send_mail(
                'We have created your listing!',
                str(email_body),
                hidden_settings.EMAIL_HOST_USER,
                [new_listing.email],
                fail_silently=False)

        return True
    except smtpLib.SMTPException:
        return False
