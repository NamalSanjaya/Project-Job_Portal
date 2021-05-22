from django.shortcuts import render,reverse,HttpResponseRedirect
from .form import RequestForm,CreateAccountForm
from .models import Seeker_Request,Seeker
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from users import views as UserView

def RequestAccount(request):

    if request.method == 'POST':
        formRA = RequestForm( request.POST , request.FILES )

        if formRA.is_valid():
            formRA.save()
            return render(request,'Seeker/request_account_message.html')
        
    else:
        formRA = RequestForm()

    context = {'formRA':formRA}
    return render(request,'Seeker/request_account.html' , context )
        
def SendMail(request, code):

    Info1   =  Seeker_Request.objects.get( token = code )
    subject, from_email , to = 'Test_Email ' , 'namaltest98@gmail.com' , [Info1.email]
    body = render_to_string( "Seeker/Email_Body.html" , { 'name' : Info1.name  ,'code':code } )
    msg = EmailMultiAlternatives(subject, body , from_email , to )                       
    msg.content_subtype = "html"
    msg.send()

    return render(request , 'Seeker/Email_Confirm.html'  )

def CreateAccount(request,code):
    
    if request.method == 'POST':
        formCA = CreateAccountForm(request.POST)
        
        if formCA.is_valid():
            NewSeeker = formCA.save(commit = False)
            if code is not None:
                Info2 =  Seeker_Request.objects.get( token = code )
                NewSeeker.fullname    = Info2.name ; NewSeeker.email = Info2.email
                NewSeeker.contact_no    = Info2.contact_no ; NewSeeker.doc_Local_Police = Info2.doc_Local_Police
                NewSeeker.doc_Gramma_Niladari = Info2.doc_Gramma_Niladari 
                NewSeeker.doc_Divisional_Secretary = Info2.doc_Divisional_Secretary
                NewSeeker.skills = Info2.skills

                details = { 'username' : request.POST['username'] , 'password' : request.POST['password'] , 'userType':"EMPLOYEE"}
                UserView.register(details)

                NewSeeker.save()
                Info2.delete()
                code = None
                
            return HttpResponseRedirect(reverse('dashboard:dashboard-home') )

    else:
        formCA = CreateAccountForm()

    return render(request,'Seeker/create_account.html', {'code': code} )

