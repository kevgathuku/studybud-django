from django.db import models


class Room(models.Model):
    # host
    # topic
    name = models.CharField(max_length=200)
    # null is for the DB. Blank allows the form field to be empty
    description = models.TextField(null=True, blank=True)
    # participants
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
