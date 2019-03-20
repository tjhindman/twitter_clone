"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import homepage, login_view, logout_link, profile, tweet
from .twitteruser.urls import urlpatterns as userurls
from .tweet.urls import urlpatterns as tweeturls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('login/', login_view),
    path('logout/', logout_link),
    path('profile/<int:user_id>', profile),
    path('tweet/<int:tweet_id>', tweet)
]

urlpatterns += userurls
urlpatterns += tweeturls
