from django import forms
from instagram.models import Post, Comments
from pyuploadcare.dj.forms import ImageField

class Uploadindexphotoform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']