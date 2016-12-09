"""GroupsApp Models

Created by Naman Patwari on 10/10/2016.
"""
from django.db import models
from AuthenticationApp.models import MyUser
from ProjectsApp.models import Project
from CommentsApp.models import Comment

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    experience = models.IntegerField(default='0')
    members = models.ManyToManyField(MyUser)
    project = models.ManyToManyField(Project)
    #comments = models.ManyToManyField(Comment)

  #  def get_experience(self):
  #      return self.experience

    def __str__(self):
        return self.name

class GroupComment(models.Model):
    commentid = models.AutoField(primary_key=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, null=True, blank=True, )
    createdat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name