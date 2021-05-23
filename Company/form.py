from django import forms
from .models import Company_Request,Company

class RequestForm(forms.ModelForm):

    class Meta:
        model = Company_Request
        exclude = ['token']
    

class CreateAccountForm(forms.ModelForm):
    
    password   = forms.CharField( )

    class Meta:
        model = Company
        fields = ['password']

class ProfileEditFormC(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['company_name' , 'registered_no' , 'address' , 'email' ,'contact_no' ]