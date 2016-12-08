"""GroupsApp Admin

Created by Naman Patwari on 10/10/2016.
"""
from django.contrib import admin

# Register your models here.
from . import models
from ProjectsApp.models import Project

admin.site.register(models.Group)
