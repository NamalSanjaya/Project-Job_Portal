from django.urls import path
from . import views
from users import views as UserView

app_name = 'seeker'

urlpatterns = [ 
    
    path('request-account/' , views.RequestAccount , name='RequestAccount'),
    path( 'sendmail/<str:code>/' , views.SendMail  , name = 'SendMail'),
    path( 'create-account/<str:code>/' , views.CreateAccount  , name = 'CreateAccount'),
    path( 'login/'  , UserView.LoginFunction , name = 'LoginSeeker' )

]

