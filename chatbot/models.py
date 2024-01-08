from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Chat(models.Model):
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField()

