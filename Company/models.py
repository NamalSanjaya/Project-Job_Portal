from django.db import models
from django.utils import timezone
from secrets import token_hex

def secret_token():
    return token_hex(8)

class Company_Request(models.Model):

    registered_name = models.CharField(max_length=30)
    registered_no   = models.CharField(max_length=20)
    address         = models.CharField(max_length=50)
    email           = models.EmailField()
    contact_no      = models.CharField(max_length = 20)
    date_requested  = models.DateTimeField(default = timezone.now)
    doc_Buisness    = models.FileField( upload_to = "Company/Company_Request/%d/" )
    token           = models.CharField( max_length = 16 , default = secret_token )

    def __str__(self):
        return self.registered_name

    def Requested_Date(self):
        return self.date_requested.date()

class Company(models.Model):

    company_name    = models.CharField(max_length=30)
    password        = models.CharField(max_length=30)
    registered_no   = models.CharField(max_length=20)
    address         = models.CharField(max_length=50)
    email           = models.EmailField()
    contact_no      = models.CharField(max_length = 20)
    date_saved      = models.DateTimeField(default = timezone.now)
    doc_buisness    = models.FileField( upload_to = "Company/Company_Request/%d/" )

    def __str__(self):
        return self.company_name

    def Saved_Date(self):
        return self.date_saved.date()


