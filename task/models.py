from email.policy import default
from django.db import models

# Create your models here.


class SlackModel(models.Model):
    slackUsername = models.CharField(max_length=30)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.CharField(max_length=255)

