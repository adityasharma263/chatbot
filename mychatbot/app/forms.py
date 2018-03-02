from django import forms

class FormData(forms.Form):
    messageText = forms.CharField(label='messageText', max_length=100)