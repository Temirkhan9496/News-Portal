from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Article, Category
from django.contrib.auth.models import User
from django.urls import reverse

@receiver(post_save, sender=User)
def add_to_common_group(sender, instance, created, **kwargs):
    if created:
        common_group = Group.objects.get(name='common')
        instance.groups.add(common_group)

@receiver(post_save, sender=Article)
def send_new_article_notification(sender, instance, created, **kwargs):
    if created:
        category = instance.category
        subscribers = category.subscribers.all()
        for user in subscribers:
            subject = f'New article in category {category.name}'
            context = {
                'article': instance,
                'category': category,
                'user': user,
            }
            html_message = render_to_string('news/new_article_email.html', context)
            plain_message = strip_tags(html_message)
            send_mail(
                subject,
                plain_message,
                'from@example.com',
                [user.email],
                html_message=html_message,
            )

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to News Portal'
        context = {'user': instance}
        html_message = render_to_string('news/welcome_email.html', context)
        plain_message = strip_tags(html_message)
        send_mail(
            subject,
            plain_message,
            'from@example.com',
            [instance.email],
            html_message=html_message,
        )