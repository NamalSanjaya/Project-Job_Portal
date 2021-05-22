from django.shortcuts import render,HttpResponseRedirect,reverse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .form import RequestForm,CreateAccountForm
from .models import Company_Request,Company
from django.contrib.auth.models import User
from users import views as UserView

def RequestAccount(request):

    if request.method == 'POST':
        formRA = RequestForm( request.POST , request.FILES )

        if formRA.is_valid():
            formRA.save()
            return render(request,'Company/request_account_message.html')

    else:
        formRA = RequestForm()

    context = {'formRA':formRA}
    return render(request,'Company/request_account.html' , context )
   
def SendMail(request, code):

    Info1   =  Company_Request.objects.get( token = code )
    subject, from_email , to = 'Test_Email' , 'namaltest98@gmail.com' , [Info1.email]
    body = render_to_string( "Company/Email_Body.html" , { 'name' : Info1.registered_name , 'number' : Info1.registered_no ,'code':code } )
    msg = EmailMultiAlternatives(subject, body , from_email , to )                       
    msg.content_subtype = "html"
    msg.send()

    return render(request , 'Company/Email_Confirm.html'  )

def CreateAccount(request,code):
    
    if request.method == 'POST':
        formCA = CreateAccountForm(request.POST)

        if formCA.is_valid():
            NewCompany = formCA.save(commit = False)
            if code is not None:
                Info2 =  Company_Request.objects.get( token = code )
                NewCompany.company_name    = Info2.registered_name ; NewCompany.registered_no = Info2.registered_no
                NewCompany.address    = Info2.address ; NewCompany.email = Info2.email 
                NewCompany.contact_no = Info2.contact_no
                NewCompany.doc_buisness = Info2.doc_Buisness

                details = { 'username' : Info2.registered_name , 'password' : request.POST['password'] , 'userType':"EMPLOYER"}
                UserView.register(details)
                NewCompany.save()
                Info2.delete()
                code = None
            return HttpResponseRedirect(reverse('dashboard:dashboard-home') )

    else:
        formCA = CreateAccountForm()

    return render(request,'Company/create_account.html', {'code': code} )