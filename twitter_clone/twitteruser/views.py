from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import TwitterUser
from .forms import Signup


def signup(request):
    form = None

    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['username'],
                data['email'],
                data['password']
            )

            login(request, user)

            TwitterUser.objects.create(
                user=user,
                username=data['username'],
                email=data['email']
            )

            return HttpResponseRedirect(reverse('mainpage'))
    else:
        form = Signup()

    return render(request, 'templates/generic_form.html', {'form': form})
