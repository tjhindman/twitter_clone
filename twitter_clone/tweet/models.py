from django.db import models
from twitter_clone.twitteruser.models import TwitterUser


class Tweet(models.Model):
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tweet = models.CharField(max_length=140)
