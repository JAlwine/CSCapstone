"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from . import forms
from ProjectsApp.models import Project
from CommentsApp.models import Comment

def getGroupComment(request):
    in_groupid = int(request.GET.get('id', '0'))
    group = models.Group.objects.filter(id__exact=in_groupid)[0]
    comment = models.GroupComment(group=group, comment=request.POST.get('comment'), user=request.user)
    comment.save()
    return HttpResponseRedirect('/group?name=%s' % group.name)

def removeGroupComment(request):
    in_name = request.GET.get('rdr', 'None')
    commentid = request.GET.get('id', 'None')
    comment = models.GroupComment.objects.get(commentid__exact=commentid)
    comment.delete()
    return HttpResponseRedirect('/group?name=%s' % in_name)

def getGroups(request):
    if request.user.is_authenticated():
        groups_list = models.Group.objects.all()
        #comments = Comment.objects.all()
        context = {
            'groups' : groups_list,
            #'comments' : comments
        }
        return render(request, 'groups.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email)
        projects = Project.objects.all()
        comments = models.GroupComment.objects.filter(group_id=in_group.id)
        context = {
            'group' : in_group,
            'userIsMember': is_member,
            'projects' : projects,
            'comments' : comments,
            'currentUser': request.user
        }
        return render(request, 'group.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroupForm(request):
    if request.user.is_authenticated() and request.user.user_type == 'STU':
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getGroupFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.GroupForm(request.POST)
            if form.is_valid():
                if models.Group.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'groupform.html', {'error' : 'Error: That Group name already exists!'})
                new_group = models.Group(name=form.cleaned_data['name'], description=form.cleaned_data['description'],
                                         experience = form.cleaned_data['experience'])
                new_group.save()
                context = {
                    'name' : form.cleaned_data['name'],
                }
                return render(request, 'groupformsuccess.html', context)
        else:
            form = forms.GroupForm()
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def joinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.members.add(request.user)
        projects = Project.objects.all()
        comments = Comment.objects.all()
        in_group.save();
        request.user.group_set.add(in_group)
        request.user.save()
        context = {
            'group' : in_group,
            'userIsMember': True,
            'projects' : projects,
            'comments' : comments
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')
    
def unjoinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.members.remove(request.user)
        projects = Project.objects.all()
        comments = Comment.objects.all()
        in_group.save();
        request.user.group_set.remove(in_group)
        request.user.save()
        context = {
            'group' : in_group,
            'userIsMember': False,
            'projects' : projects,
            'comments' : comments,
            'currentUser': request.user.id
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')

def removeGroup(request):
    if request.user.is_authenticated():
        in_group_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_group_name)
        in_group.delete()

        groups_list = models.Group.objects.all()
        context = {
            'groups': groups_list,
        }
        return render(request, 'groups.html', context)
    return render(request, 'autherror.html')
    