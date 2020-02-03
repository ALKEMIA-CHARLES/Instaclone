from django import forms
from instagram.models import Post, Comments, Profile
from pyuploadcare.dj.forms import ImageField
from django.contrib.auth.models import User

class Uploadindexphotoform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserUpdateForm(forms.ModelForm):

    class Meta: 
        model = User
        fields = ['username']

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ['comment']