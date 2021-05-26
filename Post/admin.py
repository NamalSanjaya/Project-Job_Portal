from django.contrib import admin
from .models import Post

# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display = [ 'category' , 'title' , 'owner']


admin.site.register(Post  , postAdmin)