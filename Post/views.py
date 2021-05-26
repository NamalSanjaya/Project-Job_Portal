from django.shortcuts import render
from .form import PostCreatForm
from django.http import HttpResponseNotFound
from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib import messages
from Company.models import Company

def PostCreation(request , ref):

    if ref !=1 :
        return HttpResponseNotFound('<h1>Page not found</h1>')

    if request.method == 'POST':

        formP = PostCreatForm( request.POST  , request.FILES )
       
        if formP.is_valid():
            formP.save() 
            messages.success(request,f'Successfully Post Created..')

            return HttpResponseRedirect(reverse('dashboard:dashboard-home') )

    else:
        formP = PostCreatForm( initial = { 'owner': request.user } )

    context = {'formP': formP }
    return render(request , 'Post/create_post.html' , context )
