from django import forms
from .models import Seeker_Request , Seeker

class RequestForm(forms.ModelForm):

    class Meta:
        model = Seeker_Request
        exclude = ['token']

class CreateAccountForm(forms.ModelForm):
    username   = forms.CharField( )
    password   = forms.CharField(  )

    class Meta:
        model = Seeker
        fields = ['username' , 'password']
