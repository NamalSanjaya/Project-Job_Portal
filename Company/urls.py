from django.urls import path
from . import views
from users import views as UserView

app_name = 'company'

urlpatterns = [ 
    
    path('request-account/' , views.RequestAccount , name='RequestAccount'),
    path( 'sendmail/<str:code>/' , views.SendMail  , name = 'SendMail'),
    path( 'create-account/<str:code>/' , views.CreateAccount  , name = 'CreateAccount'),
    path( 'login/<int:ref>/'  ,  UserView.LoginFunction , name = 'LoginCompany' ),
    path( 'profile/<int:ref>' , UserView.ProfileShow , name  = "ProfileShowCompany" ),
    path( 'profile-edit/<int:ref>' , UserView.ProfileEditCompany , name = "ProfileEditCompany")
    
]

