from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model('auth.Group')
    Permission = apps.get_model('auth.Permission')

    common, _ = Group.objects.get_or_create(name='common')
    authors, _ = Group.objects.get_or_create(name='authors')

    add_post = Permission.objects.get(codename='add_post')
    change_post = Permission.objects.get(codename='change_post')

    authors.permissions.add(add_post, change_post)

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_auto_20200423_1540'),  # Зависимость от предыдущих миграций
        ('news', '0001_initial'),  # Зависимость от миграций вашего приложения
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
    from __future__ import absolute_import, unicode_literals

    # Эта строка позволяет применять нижеуказанные настройки.
    from .celery import app as celery_app

    __all__ = ('celery_app',)