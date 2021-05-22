from django.contrib import admin
from .models import Seeker_Request,Seeker
from django.http import HttpResponseRedirect

def Accept(modeladmin, request, queryset):

    for data in queryset:
        code = data.token
        return HttpResponseRedirect('http://127.0.0.1:8000/employee/sendmail/%s/' %( code ))

class SeekerRequestAdmin(admin.ModelAdmin):
    list_display = ( 'name' ,  "email"  , "Requested_Date")
    list_filter = ['date_requested']
    date_hierarchy = 'date_requested'
    actions = [ Accept ]

class SeekerAdmin(admin.ModelAdmin):
    list_display = ( 'fullname' ,  "email"  , "Saved_Date")
    list_filter = ['date_saved']
    date_hierarchy = 'date_saved'


admin.site.site_header = "Job Portal Admin"
admin.site.register(Seeker_Request , SeekerRequestAdmin)
admin.site.register(Seeker  , SeekerAdmin)
#admin.site_unregister(Group)