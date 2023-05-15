from django.urls import  path
from . import  views

urlpatterns=[
    path('show_teachers',views.show_teachers,name='show_teachers'),
    path('show_students',views.show_students,name='show_students'),
    path('delete_teacher/<int:id>',views.delete_teacher,name="delete_teacher"),
    path('delete_student/<int:id>',views.delete_student,name="delete_student"),
    path('sent_review_student',views.sent_review_student,name='sent_review_student'),
    path('sent_review_teacher',views.sent_review_teacher,name='sent_review_teacher'),
    path('show_reviews',views.show_reviews,name='show_reviews'),
    path('delete_review/<int:id>',views.delete_review,name="delete_review"),
    path('teacher_approved',views.teacher_approved,name="teacher_approved"),
    path('t_approved/<int:id>',views.t_approved,name="t_approved"),
    path('t_reject/<int:id>',views.t_reject,name="t_reject"),




]