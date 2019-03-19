from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import Login
from .twitteruser.models import TwitterUser
from .tweet.models import Tweet


@login_required()
def homepage(request):
    tweets = Tweet.objects.all()

    return render(request, 'homepage.html', {'user': request.user, 'tweets': tweets})


def login_view(request):
    form = None

    if request.method == 'POST':
        form = Login(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )

            if user is not None:
                login(request, user)

                return HttpResponseRedirect(request.GET.get('next', '/'))

    else:
        form = Login()

    return render(request, 'login_form.html', {'form': form})


def logout_link(request):
    logout(request)

    return HttpResponseRedirect(request.GET.get('next', '/'))


def profile(request, user_id):
    t_user = TwitterUser.objects.filter(id=user_id)
    tweets = Tweet.objects.filter(id=user_id)

    return render(request, 'profile.html', {'user': t_user, 'tweets': tweets})


# def tweet(request, tweet_id):
#     tweets = Tweet.objects.filter(id=tweet_id)
