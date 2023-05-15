from django.shortcuts import render,redirect
from teacher.models import *
from student.models import *
from . models import *
import datetime
# Create your views here.

def show_teachers(request):
    teachers=teacher_register.objects.all()
    return render(request,'teachers.html',{'teachers':teachers})

def delete_teacher(request,id):
    teacher=teacher_register.objects.get(pk=id)
    teacher.delete()
    return redirect(show_teachers)

def show_students(request):
    students=student_register.objects.all()
    return render(request,'students.html',{'students':students})

def delete_student(request,id):
    student=student_register.objects.get(pk=id)
    student.delete()
    return redirect(show_students)

def sent_review_student(request):
    user="Student"
    name=request.session['name']
    if request.method == 'POST':
        message=request.POST.get('message')
        r_date=datetime.date.today()  
        cmt=app_review(name=name,user=user,message=message,r_date=r_date)
        cmt.save()
    return redirect('/')

def sent_review_teacher(request):
    user="Tutor"
    name=request.session['name']
    if request.method == 'POST':
        message=request.POST.get('message')
        r_date=datetime.date.today()  
        cmt=app_review(name=name,user=user,message=message,r_date=r_date)
        cmt.save()
    return redirect('/')

def show_reviews(request):
    reviews=app_review.objects.all()
    return render(request,'app_reviews.html',{'reviews':reviews})

def delete_review(request,id):
    reviews=app_review.objects.get(pk=id)
    reviews.delete()
    return redirect(show_reviews)

def teacher_approved(request):
    ap=teacher_register.objects.filter(approvedsts='NO')
    return render(request,'approved.html',{'ap':ap})


def t_approved(request,id):
    u=teacher_register.objects.get(pk=id)
    name=u.name
    age=u.age
    qualification=u.qualification
    subject=u.subject
    experience=u.experience
    fee=u.fee
    email=u.email
    place=u.place
    mobile=u.mobile
    password1=u.password1
    password2=u.password2
    image=u.image
    approvedsts='YES'
    
    reg=teacher_register(name=name,age=age,qualification=qualification,subject=subject,experience=experience,fee=fee,
                         email=email,place=place,mobile=mobile,password1=password1,password2=password2,image=image,approvedsts=approvedsts,id=id)
    reg.save()
    return redirect(teacher_approved)


def t_reject(request,id):
    u=teacher_register.objects.get(pk=id)
    name=u.name
    age=u.age
    qualification=u.qualification
    subject=u.subject
    experience=u.experience
    fee=u.fee
    email=u.email
    place=u.place
    mobile=u.mobile
    password1=u.password1
    password2=u.password2
    image=u.image
    approvedsts='CANCEL'
    
    reg=teacher_register(name=name,age=age,qualification=qualification,subject=subject,experience=experience,fee=fee,
                         email=email,place=place,mobile=mobile,password1=password1,password2=password2,image=image,approvedsts=approvedsts,id=id)
    reg.save()
    return redirect(teacher_approved)