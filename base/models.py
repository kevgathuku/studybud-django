from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # null is for the DB. Blank allows the form field to be empty
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User,
        related_name='participants',
        blank=True
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Order by the most recently updated, then order by most recently created
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # CASCADE - Delete messages when the associated Room is deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.body[0:50]
