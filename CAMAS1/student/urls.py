from django.conf.urls import include, url
from . import views

urlpatterns = [
               url(r'^$', views.students_list, name='student_list'),
               url(r'^inactive/students/$', views.students_list, name='student_list'),
               url(r'^student/(?P<pk>[0-9]+)/', views.student_profile, name='student_profile'),
               url(r'^/register/$', views.register_student, name='register_student'),
               url(r'^/edit/$', views.register_student, name='register_student'),
    ]