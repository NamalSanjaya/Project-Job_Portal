from django.shortcuts import render
from .form import PostCreatForm,PostEditForm
from django.http import HttpResponseNotFound
from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib import messages
from Company.models import Company
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name = 'dashboard:dashboard-home')
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

@login_required(redirect_field_name = 'dashboard:dashboard-home')
def ShowAllPosts(request,userName):
    try:
        ownerPK = Company.objects.get( company_name = userName )
        AllPosts = Post.objects.filter( owner = ownerPK )
    except:
        AllPosts = []
    
    return render( request  , 'Post/see_all.html' , { 'AllPosts':AllPosts } )
        


@login_required(redirect_field_name = 'dashboard:dashboard-home')
def ShowPost(request,prmKey):
    
    context = { 'Info' : Post.objects.get(pk=prmKey) }

    return render( request , 'Post/see_post.html' , context)
    

@login_required(redirect_field_name = 'dashboard:dashboard-home')
def PostEdit(request , prmKey):

    
    if request.method == 'POST':
        postExist = Post.objects.get(pk = prmKey)
        formPE = PostEditForm( request.POST , request.FILES   , instance = postExist)

        if formPE.is_valid():
            formPE.save()
            messages.success(request,f'Successfully Post Updated..')
            return HttpResponseRedirect( reverse('dashboard:dashboard-home') )
        

    else:
        postExist = Post.objects.get(pk = prmKey)
        formPE = PostEditForm(instance = postExist)

    contextPE = { 'formPE' : formPE }
    return render(request , 'Post/edit_post.html' , contextPE )

@login_required(redirect_field_name = 'dashboard:dashboard-home')
def PostDeleteConfirm(request , prmKey):
    return render(request , 'Post/delete_confirm.html' , {'prmKey' : prmKey })

@login_required(redirect_field_name = 'dashboard:dashboard-home')
def PostDelete(request , prmKey):

    postObj = Post.objects.get(pk=prmKey)
    postObj.delete()

    messages.success(request,f'Successfully deleted!')
    return HttpResponseRedirect(reverse('dashboard:dashboard-home') )


