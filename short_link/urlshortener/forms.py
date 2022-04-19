from django import forms

from .models import ShortUrl


class ShortForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))

    class Meta:
        model = ShortUrl

        fields = ('long_url',)