"""AuthenticationApp URL Configuration"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.auth_login, name='Login'),
    url(r'^logout$', views.auth_logout, name='Logout'),
    url(r'^register$', views.select_usertype, name='Register'),
    url(r'^registerStu$', views.auth_register_student, name='RegisterStu'),
    url(r'^registerTeach$', views.auth_register_teacher, name='RegisterTeach'),
    url(r'^registerEngineer$', views.auth_register_engineer, name='RegisterEngineer'),
    url(r'^update$', views.update_profile, name='UpdateProfile'),
    url(r'^profile$', views.getProfile, name='Profile'),
    url(r'^profiles$', views.getProfiles, name='Profiles'),
]
