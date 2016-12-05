"""ProjectsApp Views

Created on 10/02/16.
"""
from django.shortcuts import render

from . import models
from . import forms
from GroupsApp.models import Group
import datetime

def getProjects(request):
	projects_list = models.Project.objects.all()
	return render(request, 'projects.html', {
        'projects': projects_list,
	})



def getProject(request):
	in_name = request.GET.get('name', None)
	in_project = models.Project.objects.get(name__exact=in_name)
	is_member = in_project.createdBy.filter(email__exact=request.user.email)
	groups_list = Group.objects.all()
	assigned_groups = in_project.project_groups.all()
	context = {
		'project': in_project,
		'userIsMember': is_member,
		'groups_list': groups_list,
		'assigned_groups': assigned_groups
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
		if request.method == 'POST':
			form = forms.ProjectForm(request.POST)
			if form.is_valid():
				if models.Project.objects.filter(name__exact=form.cleaned_data['name']).exists():
					return render(request, 'projectform.html', {'error': 'Error: That Project name already exists!'})
				new_project = models.Project(name=form.cleaned_data['name'], description=form.cleaned_data['description'],
											 languages=form.cleaned_data['languages'], experience=form.cleaned_data['experience'],
											 speciality=form.cleaned_data['speciality'])
				new_project.created_at = datetime.datetime.now()
				new_project.updated_at = datetime.datetime.now()
				new_project.createdBy.add(request.user)
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


