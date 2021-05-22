from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login


def register(details):

    newUser = User()
    newUser.username   = details['username']
    newUser.set_password( details['password'] )
    newUser.first_name = details['userType' ]

    newUser.save()
    
def LoginFunction(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard:dashboard-home') )

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username , password = password )

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('dashboard:dashboard-home') )

        else:
            form = AuthenticationForm()

    else:
        form = AuthenticationForm()

    return render(request , 'users/LoginForm.html' , {'form':form} )

