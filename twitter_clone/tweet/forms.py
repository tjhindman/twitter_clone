from django import forms


class NewTweet(forms.Form):
    tweet = forms.CharField(max_length=140, widget=forms.Textarea)
