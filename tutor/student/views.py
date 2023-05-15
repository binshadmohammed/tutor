from django.shortcuts import render,redirect
from . models import *
from teacher.models import *
from django.contrib import messages
import datetime
from datetime import date
# Create your views here.



def studentsreg(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        sclass=request.POST.get('sclass')
        place=request.POST.get('place')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1 == password2:
            reg=student_register(name=name,age=age,sclass=sclass,place=place,email=email,password1=password1,password2=password2)
            reg.save()
        else:
            messages.info(request,"Incorrect Password")
    return render(request, 'studentregister.html')

def teacherdetails(request,id):
    t=teacher_register.objects.get(pk=id)
    cmt=comments.objects.filter(t_id=id)
    return render(request,'teacherdetails.html',{'t':t,'cmt':cmt})

def book_teacher(request,id):
    book=teacher_register.objects.get(pk=id)
    today = date.today().strftime('%Y-%m-%d')
    return render(request,'booking.html',{'book':book,'today':today})

def bbook_teacher(request):
    s_id=request.session['uid']
    if request.method == 'POST':
        t_id=request.POST.get('t_id')
        tname=request.POST.get('tname')
        tfee=request.POST.get('tfee')
        tplace=request.POST.get('tplace')
        tmobile=request.POST.get('tmobile')
        name=request.POST.get('name')
        address=request.POST.get('address')
        place=request.POST.get('place')
        sclass=request.POST.get('sclass')
        subject=request.POST.get('subject')
        topic=request.POST.get('topic')
        mobile=request.POST.get('mobile')
        date=request.POST.get('date')
        s_time=request.POST.get('s_time')
        e_time=request.POST.get('e_time')
        status="Pending"
        book=booking(s_id=s_id,t_id=t_id,name=name,address=address,place=place,
                     sclass=sclass,subject=subject,topic=topic,mobile=mobile,
                     date=date,s_time=s_time,e_time=e_time,status=status,tname=tname,
                     tfee=tfee,tplace=tplace,tmobile=tmobile)
        book.save()
    return redirect("/")
       
def s_bookings(request):
    s_id=request.session['uid']
    st=booking.objects.filter(s_id=s_id,status="Pending")
    return render(request,'s_bookings.html',{'st':st})

def rejected_cancelled(request):
    s_id=request.session['uid']
    rej=booking.objects.filter(s_id=s_id,status="Rejected")
    t_can=booking.objects.filter(s_id=s_id,status="Cancelled By Teacher")
    s_can=booking.objects.filter(s_id=s_id,status="Cancelled By Student")
    return render(request,'rejected_cancelled.html',{'rej':rej,'t_can':t_can,'s_can':s_can})

def sconfirm_bookings(request):
    s_id=request.session['uid']
    con=booking.objects.filter(s_id=s_id,status="Approved")
    return render(request,'sconfirm_bookings.html',{'con':con})


def student_cancel(request,id):
    upt=booking.objects.get(pk=id)
    a=upt.t_id
    b=upt.tname
    c=upt.tfee
    d=upt.tplace
    e=upt.tmobile
    f=upt.s_id
    g=upt.name
    h=upt.address
    i=upt.place
    j=upt.sclass
    k=upt.subject
    l=upt.topic
    m=upt.mobile
    n=upt.date
    o=upt.s_time
    p=upt.e_time
    q="Cancelled By student"
    reg=booking(t_id=a,tname=b,tfee=c,tplace=d,tmobile=e,s_id=f,name=g,address=h,
                place=i,sclass=j,subject=k,topic=l,mobile=m,date=n,s_time=o,e_time=p,status=q,id=id)
    reg.save()
    return redirect(s_bookings)

def sent_comment(request):
    s_id=request.session['uid']
    name=request.session['name']
    if request.method == 'POST':
        message=request.POST.get('message')
        t_id=request.POST.get('t_id')
        sdate=datetime.date.today()  
        cmt=comments(name=name,s_id=s_id,t_id=t_id,message=message,sdate=sdate)
        cmt.save()
    return redirect('/')


