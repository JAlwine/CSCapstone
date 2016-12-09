"""ProjectsApp Views

Created on 10/02/16.
"""
from django.shortcuts import render

from . import models
from . import forms
from GroupsApp.models import Group
from AuthenticationApp.models import Bookmark
from AuthenticationApp.models import MyUser
from ProjectsApp.models import Project

import datetime

def removeProjectComment(request):
	return 0

def getProjectComment(request):
	return 0

def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
		'projects': projects_list,
	})

def getBookmarks(request):
	if (request.user.is_authenticated()):
		bookmarks_list = Bookmark.objects.all()
		pIdsToGet = [bookmark.projectID for bookmark in bookmarks_list if bookmark.userID == request.user.id]
		projects_list = Project.objects.filter(id__in=pIdsToGet)
		context = {
			'projects' : projects_list
		}
		return render(request, 'bookmarks.html', context)
	return render(request, 'autherror.html')


def bookmarkProject(request):
	if (request.user.is_authenticated()):
		in_projectName = request.GET.get('name', 'None')
		in_project = Project.objects.get(name__exact=in_projectName)
		in_user = MyUser.objects.get(email__exact=request.user.email)
		try:
			this_bookmark = Bookmark.objects.get(userID=request.user.id, projectID=in_project.id)
			this_bookmark.delete()
		except:
			in_bookmark = Bookmark()
			in_bookmark.projectID = in_project.id
			in_bookmark.userID = in_user.id
			in_bookmark.save()

		context = {
			'project' : in_project
		}
		return render(request, 'project.html', context)

	return render(request, 'autherror.html')

def getProject(request):
	in_name = request.GET.get('name', None)
	in_project = models.Project.objects.get(name__exact=in_name)
	is_member = in_project.createdBy
	groups_list = Group.objects.all()
	# assigned_groups = in_project.project_groups.all()
	context = {
		'project': in_project,
		'userIsMember': is_member,
		'groups_list': groups_list,
		# 'assigned_groups': assigned_groups
	}
	if request.method == 'POST':
		group_names = request.POST.getlist('dropdownl', 'None')
		if group_names != 'None':
			for group_name in group_names:
				group = Group.objects.get(name__exact=group_name)
				group.project.add(in_project)
				print
				group.project
				group.save()
		else:
			return render(request, 'autherror.html')

	return render(request, 'project.html', context)


def getProjectForm(request):
	if request.user.is_authenticated():
		return render(request, 'projectform.html')
	# render error page if user is not logged in
	return render(request, 'autherror.html')


def getProjectFormSuccess(request):
	print("In function")
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = forms.ProjectForm(request.POST)
			print(form.errors)
			if form.is_valid():
				if models.Project.objects.filter(name__exact=form.cleaned_data['name']).exists():
					return render(request, 'projectform.html', {'error': 'Error: That Project name already exists!'})
				new_project = models.Project(name=form.cleaned_data['name'], description=form.cleaned_data['description'],
											 languages=form.cleaned_data['languages'], experience=form.cleaned_data['experience'],
											 speciality=form.cleaned_data['speciality'], createdBy=request.user.email)
				new_project.created_at = datetime.datetime.now()
				new_project.updated_at = datetime.datetime.now()
				new_project.save()
				request.user.save()
				context = {
					'name': form.cleaned_data['name'],
				}
				return render(request, 'projectformsuccess.html', context)
		else:
			form = forms.ProjectForm()
		return render(request, 'projectform.html')
	# render error page if user is not logged in
	return render(request, 'autherror.html')

def removeProject(request):
	if request.user.is_authenticated():
		in_project_name = request.GET.get('name', 'None')
		in_project = models.Project.objects.get(name__exact=in_project_name)
		in_project.delete()

		projects_list = models.Project.objects.all()
		return render(request, 'projects.html', {
			'projects': projects_list,
		})

	return render(request, 'autherror.html')


