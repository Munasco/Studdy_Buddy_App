from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from datetime import datetime as dt


# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    avatar = models.FileField(null=True, upload_to='images/%Y/%m/',
                              validators=[FileExtensionValidator(['png', 'jpg', 'svg'])],  default=f'images/avatar.svg')


class Topic(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='host_rooms')
    topic = models.ForeignKey(
        'Topic', on_delete=models.SET_NULL, null=True, related_name="topic_rooms")
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='users_rooms', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_messages")
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="messages_in_room")
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[:50]
