from django.contrib import admin
from .models import *
# Register your models here.


class teacher_regAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','qualification','subject', 'experience','fee','email','place','mobile','password1','password2','image',)
    
admin.site.register(teacher_register,teacher_regAdmin)   
    
    
     