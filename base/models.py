from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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