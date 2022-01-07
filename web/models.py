from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='UserProfiles')

    def __str__(self):
        return self.user.username
    

class Message(models.Model):
    sender = models.CharField(max_length=255, null=True, blank=True)
    thread_name = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    sender = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.name
    