from django import forms


class CapitalGuess(forms.Form):
    guess = forms.CharField(max_length=100)
