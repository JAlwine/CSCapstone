"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^project/all$', views.getProjects, name='Projects'),
    url(r'^project/form$', views.getProjectForm, name='ProjectForm'),
    url(r'^project/formsuccess$', views.getProjectFormSuccess, name='ProjectFormSuccess'),
    url(r'^project/bookmarks$', views.getBookmarks),
    url(r'^project/bookmark$', views.bookmarkProject, name='BookmarkProject'),
    url(r'^project/removecomment$', views.removeProjectComment, name='removeProjectComment'),
    url(r'^project/comment$', views.getProjectComment, name='getProjectComment'),
    url(r'^project/remove$', views.removeProject, name="removeProject"),
    url(r'^project', views.getProject, name='Project'),
]