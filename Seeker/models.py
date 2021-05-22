from django.db import models
from django import forms
from django.utils import timezone
from multiselectfield import MultiSelectField
from secrets import token_hex

MEDIA_CHOICES = [  ('Design',( ('Logo_Designer' , 'Logo Designer') , 
                                    ('Web_Designer' , 'Web Designer' ) ,
                                    ( 'Print_Designer' , 'Print Designer') , )
                        ) , 
                        ( 'Technology',( ('Mobile_App_Developer' , 'Mobile App Developer'),
                                         ( 'Software_Engineer'   , 'Software Enginner' ) ,
                                         ( 'DataBase_Engineer'   , 'DataBase Engineer') ,
                                         ( 'System_Engineer'     , 'System Engineer' ) , ) 
                        ) ,
                        ( 'Entertainment', ( ('Content_Writer' , 'Content Writer') , 
                                             ('Video_Editer' , 'Video Editer') , )
                        )    
                ]

def secret_token():
    return token_hex(8)


class Seeker_Request(models.Model):

    name                = models.CharField(max_length=20)
    email               = models.EmailField()
    contact_no          = models.CharField(max_length=20)
    date_requested      = models.DateTimeField(default = timezone.now)
    doc_Local_Police    = models.FileField( upload_to = "Seeker/Seeker_Request/%d/LP/" )
    doc_Gramma_Niladari         = models.FileField( upload_to = "Seeker/Seeker_Request/%d/GN" )
    doc_Divisional_Secretary    = models.FileField( upload_to = "Seeker/Seeker_Request/%d/DS" )
    token   = models.CharField( max_length = 16 , default = secret_token )
    skills = MultiSelectField(
        max_length = 200,
        choices=MEDIA_CHOICES,
    )

    def __str__(self):
        return self.name

    def Requested_Date(self):
        return self.date_requested.date()

class Seeker(models.Model):

    fullname            = models.CharField(max_length=20)
    username            = models.CharField(max_length=20 )
    password            = models.CharField(max_length=30 )
    email               = models.EmailField()
    contact_no          = models.CharField(max_length=20)
    date_saved          = models.DateTimeField(default = timezone.now)
    doc_Local_Police    = models.FileField( upload_to = "Seeker/Seeker_Request/%d/LP/" )
    doc_Gramma_Niladari         = models.FileField( upload_to = "Seeker/Seeker_Request/%d/GN" )
    doc_Divisional_Secretary    = models.FileField( upload_to = "Seeker/Seeker_Request/%d/DS" )
    token   = models.CharField( max_length = 16 , default = secret_token )
    skills  = MultiSelectField(
        max_length = 200,
        choices=MEDIA_CHOICES,
    )

    def __str__(self):
        return self.username

    def Saved_Date(self):
        return self.date_saved.date()

