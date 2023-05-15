from django.shortcuts import render,redirect
from  django.core.files.storage import FileSystemStorage
from django.contrib import messages
from . models import *
from student.models import *
# Create your views here

def teacher_reg(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        qualification=request.POST.get('qualification')
        subject=request.POST.get('subject')
        experience=request.POST.get('experience')
        fee=request.POST.get('fee')
        place=request.POST.get('place')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        image="profile.png"
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        approvedsts= "NO"
        if password1 == password2:
            reg=teacher_register(name=name,age=age,qualification=qualification,subject=subject,experience=experience,fee=fee,place=place,email=email,mobile=mobile,password1=password1,password2=password2,image=image, approvedsts= approvedsts)
            reg.save()
        else:
            messages.info(request,"Incorrect Password")
    return render(request, 'teacherregister.html')

# notification
def t_bookings(request):
    t_id=request.session['tid']
    student=booking.objects.filter(t_id=t_id,status="Pending")
    l=len(student)
    a=""
    if l==0:
        a="empty"
    else:
        a="yes"
    print(a)
    return render(request,'t_bookings.html',{'student':student,'a':a})

def approved(request,id):
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
    q="Approved"
    reg=booking(t_id=a,tname=b,tfee=c,tplace=d,tmobile=e,s_id=f,name=g,address=h,
                place=i,sclass=j,subject=k,topic=l,mobile=m,date=n,s_time=o,e_time=p,status=q,id=id)
    reg.save()
    return redirect(t_bookings)

def rejected(request,id):
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
    q="Rejected"
    reg=booking(t_id=a,tname=b,tfee=c,tplace=d,tmobile=e,s_id=f,name=g,address=h,
                place=i,sclass=j,subject=k,topic=l,mobile=m,date=n,s_time=o,e_time=p,status=q,id=id)
    reg.save()
    return redirect(t_bookings)

def confirm_bookings(request):
    t_id=request.session['tid']
    student=booking.objects.filter(t_id=t_id,status="Approved")
    return render(request,'confirm_bookings.html',{'student':student})


def rejected_bookings(request):
    t_id=request.session['tid']
    student=booking.objects.filter(t_id=t_id,status="Rejected")
    return render(request,'rejected.html',{'student':student})

def teacher_cancelled(request):
    t_id=request.session['tid']
    student=booking.objects.filter(t_id=t_id,status="Cancelled By Teacher")
    return render(request,'teacher_cancelled.html',{'student':student})

def teacher_cancel(request,id):
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
    q="Cancelled By Teacher"
    reg=booking(t_id=a,tname=b,tfee=c,tplace=d,tmobile=e,s_id=f,name=g,address=h,
                place=i,sclass=j,subject=k,topic=l,mobile=m,date=n,s_time=o,e_time=p,status=q,id=id)
    reg.save()
    return redirect(confirm_bookings)

def tstudent_cancel(request):
    t_id=request.session['tid']
    sc=booking.objects.filter(t_id=t_id,status="Cancelled By Student")
    return render(request,'tstudent_cancel.html',{'sc':sc})

def teacher_profile(request):
    pro=request.session['tid']
    p=teacher_register.objects.get(id=pro)
    return render(request,'teacher_profile.html',{'t':p})

def teacher_uprofile(request,id):
    p=teacher_register.objects.get(pk=id)
    return render(request,'teacher_uprofile.html',{'p':p})

def teacher_uuprofile(request,id):
    if request.method == 'POST':
        u=teacher_register.objects.get(pk=id)
        image=u.image
        name=request.POST.get('name')
        age=request.POST.get('age')
        qualification=request.POST.get('qualification')
        subject=request.POST.get('subject')
        experience=request.POST.get('experience')
        fee=request.POST.get('fee')
        place=request.POST.get('place')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        approvedsts=request.POST.get('approvedsts')
        reg=teacher_register(name=name,age=age,qualification=qualification,subject=subject,experience=experience,fee=fee,place=place,email=email,mobile=mobile,password1=password1,password2=password2,image=image,approvedsts=approvedsts,id=id)
        reg.save()
    return redirect(teacher_profile)

def t_image(request,id):
    p=teacher_register.objects.get(pk=id)
    return render(request,'add_teacher_image.html',{'p':p})

def t_uimage(request,id):
    if request.method == 'POST':
        u=teacher_register.objects.get(pk=id)
        name=u.name
        age=u.age
        qualification=u.qualification
        subject=u.subject
        experience=u.experience
        fee=u.fee
        place=u.place
        email=u.email
        mobile=u.mobile
        password1=u.password1
        password2=u.password2
        approvedsts=u.approvedsts
        image=request.FILES['image']
        a=FileSystemStorage()
        b=a.save(image.name,image)
        
        reg=teacher_register(name=name,age=age,qualification=qualification,subject=subject,experience=experience,fee=fee,place=place,email=email,mobile=mobile,password1=password1,password2=password2,image=image,approvedsts=approvedsts,id=id)
        reg.save()
    return redirect(teacher_profile)

def show_comments(request):
    c=request.session['tid']
    cmt=comments.objects.filter(t_id=c)
    return render(request,'show_comments.html',{'cmt':cmt})