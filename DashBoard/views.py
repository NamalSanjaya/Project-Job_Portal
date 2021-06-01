from django.shortcuts import render
from Company.models import Company

# Create your views here.

def Home(request):
    allC = Company.objects.all()
    Ln = len(allC)
    mx  = min(Ln , 3 )
    context = { 'SomeCompany' : Company.objects.all()[:mx] }

    return render( request , 'DashBoard/dash_board.html' , context )

