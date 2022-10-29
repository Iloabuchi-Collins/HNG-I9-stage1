from django.db import models

# Create your models here.

class SlackUser(models.Model):
    slackUsername = models.CharField(max_length = 20)
    backend = models.BooleanField()
    age = models.PositiveIntegerField(default = 0)
    bio = models.CharField(max_length = 50, blank = True)