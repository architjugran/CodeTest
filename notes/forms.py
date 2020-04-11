from django import forms
from django.contrib.auth.models import User

from .models import Note



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = [ 'title', 'description']