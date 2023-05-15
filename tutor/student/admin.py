from django.contrib import admin
from .models import *
# Register your models here.
class studentsregAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','sclass','place', 'email','password1','password2',)

admin.site.register(student_register,studentsregAdmin)
admin.site.register( booking)
admin.site.register(comments)