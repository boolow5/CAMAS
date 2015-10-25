from django.conf.urls import include, url
from . import views

urlpatterns = [
               url(r'^$', views.patient_list, name='patient_list'),
               url(r'^patient/(?P<pk>[0-9]+)/', views.patient_profile, name='patient_profile'),
               url(r'^/in/$', views.in_patient, name='in_patient'),
               url(r'^/out/$', views.out_patient, name='out_patient'),
               url(r'^/register/$', views.register_patient, name='register_patient'),
               #url(r'^/search/$', views.search_page, name = 'search_page'),

    ]