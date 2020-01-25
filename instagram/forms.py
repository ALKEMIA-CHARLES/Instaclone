from django import forms
from instagram.models import Profile, DBUSER, Comments
from pyuploadcare.dj.forms import ImageField
class Signupform(forms.ModelForm):
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
                                                               "placeholder":"First Name"}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
                                                               "placeholder":"Last Name"}))
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={
                                                               "placeholder":"Username"}))
    email = forms.CharField(label=False, widget=forms.TextInput(attrs={
                                                               "placeholder":"Email"}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={
                                                               "placeholder":"Password"}))

    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "username", "email", "password",)

class   LoggedinUserform(forms.ModelForm):
     class Meta:
        model = Profile
        fields = ("image",)
class Uploadform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'user', 'bio']

class Uploadindexphotoform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'caption']