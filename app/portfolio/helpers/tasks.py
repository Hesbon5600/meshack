import logging

from django.conf import settings

from app import celery_app
from django.core.mail import EmailMessage


@celery_app.task(name="send mail")
def send_mail_(*args):
    """
    handle sending of mails to users
    Args:
        args (list): a list of possible arguments
    Return:
        None
    """
    subject, message, from_email = args
    try:
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[settings.TO_EMAIL],
            reply_to=[from_email],
        )
        email.send(fail_silently=False)
    except Exception as e:
        logging.warning(e)
