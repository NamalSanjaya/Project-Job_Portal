from django.urls import path
from . import views
from users import views as UserView
from Post import views as PostView

app_name = 'company'

urlpatterns = [ 
    
    path('request-account/' , views.RequestAccount , name='RequestAccount'),
    path( 'sendmail/<str:code>/' , views.SendMail  , name = 'SendMail'),
    path( 'create-account/<str:code>/' , views.CreateAccount  , name = 'CreateAccount'),
    path( 'login/<int:ref>/'  ,  UserView.LoginFunction , name = 'LoginCompany' ),
    path( 'profile/<int:ref>' , UserView.ProfileShow , name  = "ProfileShowCompany" ),
    path( 'profile-edit/<int:ref>' , UserView.ProfileEditCompany , name = "ProfileEditCompany"),
    path( 'post-creation/<int:ref>' , PostView.PostCreation , name = 'PostCreationCompany' ),
    path( 'post-all-show/<str:userName>' , PostView.ShowAllPosts , name = 'ShowAllPostsCompany' ),
    path(  'post-show/<int:prmKey>' , PostView.ShowPost , name = 'ShowPostCompany' ),
    path( 'post-edit/<int:prmKey>'  ,  PostView.PostEdit  , name = 'PostEditCompany'),
    path( 'post-delete-confirm/<int:prmKey>', PostView.PostDeleteConfirm , name = 'PostDeleteConfirm'),
    path( 'post-delete/<int:prmKey>' , PostView.PostDelete , name = 'PostDelete')
    
]

