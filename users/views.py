from django.shortcuts import render,HttpResponseRedirect,reverse
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import logout
from Company.models import Company
from Seeker.models import Seeker
from django.contrib.auth.decorators import login_required
from Company.form import ProfileEditFormC
from Seeker.form import ProfileEditFormS
from . import form as user_form
def register(details):
    newUser = User()
    newUser.username   = details['username']
    newUser.set_password( details['password'] )
    newUser.first_name = details['userType']

    newUser.save()
    
def LoginFunction(request,ref):

    if ref == 1:
        objType = "EMPLOYER"
    elif ref==2:
        objType = "EMPLOYEE"
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard:dashboard-home') )

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username , password = password )

        if user is not None:
            userType = User.objects.get( username = username ).first_name

            if userType != objType:
                messages.error(request,f'logging is failed..!')
            else:
                login(request,user)
                messages.success(request,f'Successfully logged In..')
            return HttpResponseRedirect(reverse('dashboard:dashboard-home') )

        else:
            form = AuthenticationForm()

    else:
        form = AuthenticationForm()

    return render(request , 'users/LoginForm.html' , {'form':form , 'objType': objType } )


@login_required(redirect_field_name = 'dashboard:dashboard-home')
def LogoutFunction(request):
    logout(request)
    messages.success(request,f'Successfully logged out..')
    return HttpResponseRedirect(reverse('dashboard:dashboard-home') )

@login_required(redirect_field_name = 'dashboard:dashboard-home')
def ProfileShow(request , ref):
    
    if ref == 1:
        context  = { 'Item' : Company.objects.get( company_name = request.user.username )  }
        return render(request , 'users/profileEmployer.html' , context  )

    elif ref == 2:
        context  = { 'Item' : Seeker.objects.get( username = request.user.username )  }
        return render( request , 'users/profileEmployee.html' , context )

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


@login_required(redirect_field_name = 'dashboard:dashboard-home')    
def ProfileEditCompany(request,ref):

    if ref != 1:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    if request.method == 'POST':
        
        formU = ProfileEditFormC(request.POST , instance = Company.objects.get(company_name = request.user.username ) )
        
        if formU.is_valid():
            userC = User.objects.get( username = request.user.username )
            userC.username = request.POST['company_name']
            userC.save()
            formU.save()
            messages.success(request,f'Successfully Updated!')
            return HttpResponseRedirect(reverse('company:ProfileShowCompany', args=(1,) ) )

        
    else:
        formU = ProfileEditFormC( instance = Company.objects.get(company_name = request.user.username ) )

        return render(request , 'users/UpdateForm.html' ,  { 'formU' : formU })


@login_required(redirect_field_name = 'dashboard:dashboard-home') 
def ProfileEditSeeker(request,ref):

    if ref !=2 :
        return HttpResponseNotFound('<h1>Page not found</h1>')

    if request.method == 'POST':
        formU = ProfileEditFormS( request.POST , instance = Seeker.objects.get( username = request.user.username ))

        if formU.is_valid():
            userS   = User.objects.get( username = request.user.username )
            userS.username = request.POST['username']
            userS.save()
            formU.save()
            messages.success(request,f'Successfully Updated!')
            return HttpResponseRedirect( reverse('seeker:ProfileShowSeeker' , args= (2,) ))

    else:
        formU = ProfileEditFormS( instance = Seeker.objects.get( username = request.user.username ) )
    
    return render(request , 'users/UpdateForm.html' ,  { 'formU' : formU })

@login_required(redirect_field_name = 'dashboard:dashboard-home')
def DeleteConfirm(request):
    return render(request , 'users/deleteConfirm.html' )


@login_required(redirect_field_name = 'dashboard:dashboard-home') 
def ProfileDelete(request):
    us = request.user
    if us.first_name == "EMPLOYER":
        cp = Company.objects.get(company_name = us.username)
        cp.delete()
        us.delete()
        
    elif us.first_name == "EMPLOYEE":
        sk = Seeker.objects.get( username = us.username )
        sk.delete()
        us.delete()

    messages.success(request,f'Successfully deleted!')
    return HttpResponseRedirect(reverse('dashboard:dashboard-home') )
