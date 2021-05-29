from django import forms
from .models import Post


class PostCreatForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

class PostEditForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['owner']
        