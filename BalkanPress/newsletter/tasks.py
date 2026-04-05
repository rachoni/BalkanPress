from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import NewsletterSubscriber


@shared_task
def send_newsletter(subject, message):
    subscribers = NewsletterSubscriber.objects.filter(is_active=True)

    sent_count = 0
    for subscriber in subscribers:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [subscriber.email],
            fail_silently=False,
        )
        sent_count += 1

    return sent_count
