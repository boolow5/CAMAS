from django.conf.urls import include, url
from . import views

urlpatterns = [
               url(r'^teachers/$', views.teachers_list, name='teachers_list'),
               url(r'^teacher/(?P<pk>[0-9]+)/', views.teacher_profile, name='teacher_profile'),
               url(r'^new/teacher/$', views.register_teacher, name='register_teacher'),
               url(r'^edit/teacher/(?P<pk>[0-9]+)/$', views.update_teacher, name='update_teacher'),
               url(r'^$',views.index, name='index'),
               url(r'^students$', views.students_list, name='student_list'),
               url(r'^student/(?P<pk>[0-9]+)/', views.student_profile, name='student_profile'),
               url(r'^new/student/$', views.register_student, name='register_student'),
               url(r'^edit/student/(?P<pk>[0-9]+)/$', views.update_student, name='update_student'),
               url(r'^accounts/$', views.accounts_list, name='accounts_list'),
               url(r'^account/(?P<pk>[0-9]+)/$', views.account_details, name='account_details'),
               #url(r'^edit/account/(?P<pk>[0-9]+)/', views.edit_account, name='edit_account'),
               url(r'^new/account/', views.create_account, name='create_account'),
               url(r'^payments/(?P<pk>[0-9]+)/$', views.payments_list, name='payments_list'),
               url(r'^payment/(?P<pk>[0-9]+)/$', views.payment_details, name='payment_details'),
               #url(r'^edit/payment/(?P<pk>[0-9]+)/', views.edit_payment, name='edit_account'),
               url(r'^new/payment/', views.add_payment, name='add_account'),

    ]