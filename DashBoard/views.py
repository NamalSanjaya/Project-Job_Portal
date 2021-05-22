from django.shortcuts import render

# Create your views here.

def Home(request):
    return render( request , 'DashBoard/dash_board.html' )

