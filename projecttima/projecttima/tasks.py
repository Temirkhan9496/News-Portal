from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import News, Subscriber
from django.utils import timezone
from datetime import timedelta

@shared_task
def send_new_news_notification(news_id):
    news = News.objects.get(id=news_id)
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        subject = f'New Article: {news.title}'
        message = render_to_string('new_news_email.html', {'news': news})
        send_mail(subject, message, 'from@example.com', [subscriber.email])

@shared_task
def send_weekly_newsletter():
    now = timezone.now()
    week_ago = now - timedelta(days=7)
    news_list = News.objects.filter(created_at__gte=week_ago)

    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        subject = 'Weekly Newsletter'
        message = render_to_string('weekly_newsletter.html', {'news_list': news_list})
        send_mail(subject, message, 'from@example.com', [subscriber.email])
