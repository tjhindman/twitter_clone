from django.shortcuts import render
from .models import Tweet
from .forms import NewTweet


def newtweet(request):
    form = None

    if request.method == 'POST':
        form = NewTweet(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Tweet.objects.create(
                user=request.user.twitteruser,
                tweet=data['tweet']
            )

    else:
        form = NewTweet()

    return render(request, 'tweet/templates/generic_form.html', {'form': form})
