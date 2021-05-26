from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from Company.models import Company


category_choices = [
    ( 'Design','Design') , ( 'Technology' , 'Technology') , ( 'Entertainment' , 'Entertainment') 
]

title_choice = [
    ('Log_Design' , 'Log Design') , ( 'Web_Design', 'Web Design') , ( 'Print_Design','Print Design') , 
    ( 'Mobile_App_Developer', 'Mobile App Developer') , ( 'Software_Engineer' ,'Software Engineer') , 
    ( 'DataBase_Engineer' ,'DataBase Engineer'),
    ( 'System_Engineer' , 'System Engineer') , ( 'Content_Writer' , 'Content Writer') , ( 'Video_Editor' , 'Video Editor')
]



def makePath():
    return "Company/" + user.username + "/Post/"

class Post(models.Model):

    category = models.CharField(max_length = 50 , choices = category_choices)
    title    = models.CharField(max_length = 50 , choices = title_choice )
    image    = models.ImageField(upload_to = "Company/Post/" )
    descript = models.TextField(blank = True)
    owner    = models.ForeignKey( Company , on_delete = models.CASCADE )

    def __str__(self):
        return self.title + '-Post'

    def save(self,*args , **kwargs):
        super().save(*args , **kwargs)

        img = Image.open( self.image.path )

        if img.height>400 or img.width>400:
            img.thumbnail((400,400))
            img.save( self.image.path )

