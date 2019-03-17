from django.db import models
from django.contrib.auth.models import User


class TwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    followers = models.ManyToManyField(User)

    def __str__(self):
        return self.user.username
