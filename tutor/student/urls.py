from django.urls import  path
from . import  views

urlpatterns=[
    path('studentsreg',views.studentsreg,name="studentsreg"),
    path('teacherdetails/<int:id>',views.teacherdetails,name="teacherdetails"),
    path('book_teacher',views.book_teacher),
    path('book_teacher/<int:id>',views.book_teacher,name="book_teacher"),
    path('book_teacher/bbook_teacher',views.bbook_teacher,name="bbook_teacher"),
    path('s_bookings',views.s_bookings,name="s_bookings"),
    path('rejected_cancelled',views.rejected_cancelled,name="rejected_cancelled"),
    path('sconfirm_bookings',views.sconfirm_bookings,name="sconfirm_bookings"),
    path('student_cancel/<int:id>',views.student_cancel,name="student_cancel"),
    path('teacherdetails/sent_comment',views.sent_comment,name='sent_comment'),
    

]