from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    date = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True)
    finished = models.BooleanField(null=True, blank=True)