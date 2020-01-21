from django import forms
from instagram.models import loggedinUser, DBUSER, Comments

class Uploadform(forms.ModelForm):
    class Meta:
        model = loggedinUser
        fields = ['image', 'caption']