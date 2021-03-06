"""GroupsApp URL

Created by Naman Patwari on 10/10/2016.
"""
from django.conf.urls import url
from ProjectsApp.models import Project

from . import views

urlpatterns = [
    url(r'^group/all$', views.getGroups, name='Groups'),
	url(r'^group/form$', views.getGroupForm, name='GroupForm'),
    url(r'^group/formsuccess$', views.getGroupFormSuccess, name='GroupFormSuccess'),
    url(r'^group/join$', views.joinGroup, name='GJoin'),
    url(r'^group/unjoin$', views.unjoinGroup, name='GUnjoin'),
    url(r'^group/remove$', views.removeGroup, name='GRemove'),
    url(r'^group$', views.getGroup, name='Group'),
    url(r'^groupcommentremove$', views.removeGroupComment, name='removeGroupComment'),
    url(r'^group/comment$', views.getGroupComment, name='getGroupComment'),
]