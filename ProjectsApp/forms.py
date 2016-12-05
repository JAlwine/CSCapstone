"""GroupsApp Forms

Created by Naman Patwari on 10/10/2016.
"""
from django import forms
from .models import Project

class ProjectForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', widget=forms.Textarea,  max_length=3000)
    languages = forms.CharField(label='ProgrammingLanguage', max_length=300 )
    experience = forms.IntegerField(label='YearsOfExperience')
    speciality = forms.CharField(label='Speciality', widget=forms.TextInput, max_length=200, required=False)

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'languages', 'experience', 'speciality')
        widgets = {
            'description':forms.Textarea()
        }