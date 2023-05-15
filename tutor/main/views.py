from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from  django.core.files.storage import FileSystemStorage
from django.conf import settings
from student.models import *
from teacher.models import *
from adminside.models import *
from adminside.views import *
from student.views import *
from student.urls import *


def home(request):
    teacher=teacher_register.objects.filter( approvedsts="YES")
    review=app_review.objects.all()
    return render(request,'index.html',{'teacher':teacher,'review':review})


def loguser(request):
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    if email == 'admin@gmail.com' and password1 =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] ='admin'
        return redirect("/")

    elif student_register.objects.filter(email=email,password1=password1).exists():
        udetails=student_register.objects.get(email=request.POST['email'],password1=password1)
        if udetails.password1 == request.POST['password1']:
            request.session['uid'] = udetails.id
            request.session['name'] = udetails.name
            request.session['email'] = email
            request.session['user'] = "student"
            return redirect("/")

    elif teacher_register.objects.filter(email=email,password1=password1).exists():
        udetails=teacher_register.objects.get(email=request.POST['email'],password1=password1)
        if udetails.password1 == request.POST['password1']:
            request.session['tid'] = udetails.id
            request.session['name'] = udetails.name
            request.session['email'] = email
            request.session['user'] = 'teacher'
            return redirect("/")
                                                                                
    else:
        return render(request, 'login.html')


def userlogout(request):
    request.session.delete()
    return redirect("/")
 
def About(request):
    return render(request,'about.html')