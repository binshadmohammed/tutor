from django.urls import  path
from . import  views

urlpatterns=[
    
    path('teacher_reg',views.teacher_reg,name="teacher_reg"),
    path('t_bookings',views.t_bookings),
    path('approved/<int:id>',views.approved,name='approved'),
    path('rejected/<int:id>',views.rejected,name='rejected'),
    path('teacher_cancel/<int:id>',views.teacher_cancel,name="teacher_cancel"),
    path('confirm_bookings',views.confirm_bookings),
    path('rejected_bookings',views.rejected_bookings),
    path('teacher_cancelled',views.teacher_cancelled),
    path('tstudent_cancel',views.tstudent_cancel,name="tstudent_cancel"),
    path('teacher_profile',views.teacher_profile,name="teacher_profile"),
    path('teacher_uprofile/<int:id>',views.teacher_uprofile,name="teacher_uprofile"),
    path('teacher_uprofile/teacher_uuprofile/<int:id>',views.teacher_uuprofile,name="teacher_uuprofile"),
    path('t_image/<int:id>',views.t_image,name="t_image"),
    path('t_image/t_uimage/<int:id>',views.t_uimage,name="t_uimage"),
    path('show_comments',views.show_comments,name="show_comments"),


]