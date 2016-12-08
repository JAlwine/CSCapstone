"""GroupsApp Forms

Created by Naman Patwari on 10/10/2016.
"""
from django import forms
from ProjectsApp.models import Project


class GroupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)
    experience = forms.IntegerField(label='Experience')