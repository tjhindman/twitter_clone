from django.contrib import admin
from .tweet.models import Tweet
from .twitteruser.models import TwitterUser


class TweetAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.register(TwitterUser)
admin.site.register(Tweet, TweetAdmin)
