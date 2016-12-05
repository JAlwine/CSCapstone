"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from AuthenticationApp.models import MyUser
import datetime

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    languages = models.CharField(max_length=200, default="/")
    experience = models.CharField(max_length=200, default=0)
    speciality = models.CharField(max_length=200, default="/")
    createdBy = models.ManyToManyField(MyUser)
    #add a foreign key company field here

    # TODO Task 3.5: Add field for company relationship
    # TODO Task 3.5: Add fields for project qualifications (minimum required: programming language, years of experience, speciality)

    def create_project(self, name=None, description=None, created_at=str(datetime.datetime.now()),
                       updated_at=str(datetime.datetime.now()), languages=None, experience=None,
                       specialty=None, createdBy=None):

        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.languages = languages
        self.experience = experience
        self.specialty = specialty
        self.createdBy = createdBy
        self.save()
        return self

    def __str__(self):
        return self.name