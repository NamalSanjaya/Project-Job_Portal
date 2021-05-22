from django.contrib import admin
from .models import Company_Request,Company
from django.http import HttpResponseRedirect


def Accept(modeladmin, request, queryset):

    for data in queryset:
        code = data.token
        return HttpResponseRedirect('http://127.0.0.1:8000/employer/sendmail/%s/' %( code ))

class CompanyRequestAdmin(admin.ModelAdmin):
    list_display = ( 'registered_name' ,  "email" , "Requested_Date" )
    list_filter = ['date_requested']
    date_hierarchy = 'date_requested'
    actions = [ Accept ]

class CompanyAdmin(admin.ModelAdmin):
    list_display = ( 'company_name' ,  "email" , "Saved_Date" )
    list_filter = ['date_saved']


admin.site.register(Company_Request , CompanyRequestAdmin)
admin.site.register(Company , CompanyAdmin)

