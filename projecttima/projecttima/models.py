from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class User(models.Model):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    category_choices = [
        ('Танки', 'Танки'),
        ('Хилы', 'Хилы'),
        # Добавьте остальные категории
    ]
    category = models.CharField(max_length=20, choices=category_choices)

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    text = models.TextField()