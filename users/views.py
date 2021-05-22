from django.shortcuts import render,HttpResponseRedirect,reverse
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

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

