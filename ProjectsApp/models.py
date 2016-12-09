"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from CommentsApp.models import Comment

import datetime

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    languages = models.CharField(max_length=200, default="/")
    experience = models.IntegerField(default=0)
    speciality = models.CharField(max_length=200, default="/")
    createdBy = models.CharField(max_length=200, default="/")
    #add a foreign key company field here

    # TODO Task 3.5: Add field for company relationship
    # TODO Task 3.5: Add fields for project qualifications (minimum required: programming language, years of experience, speciality)



    def __str__(self):
        return self.name

class ProjectComment(models.Model):
    commentid = models.AutoField(primary_key=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, null=True, blank=True, )
    createdat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

