"""AuthenticationApp Models"""

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# from django.db.models.signals import post_save

# Create your models here.


class MyUserManager(BaseUserManager):

    def create_user(self, email=None, password=None, first_name=None, last_name=None, user_type=None, university_name=None, phone_number=None, home_address=None, about_user=None):
        if not email:
            raise ValueError('Users must have an email address')

        # We can safetly create the user
        # Only the email field is required
        user = self.model(email=email)
        user.last_name = last_name
        user.first_name = first_name
        user.user_type=user_type
        user.university_name=university_name
        user.phone_number=phone_number
        user.home_address=home_address
        user.about_user=about_user

        user.set_password(password)


        # If first_name is not present, set it as email's username by default
        if first_name is None or first_name == "" or first_name == '':
            user.first_name = email[:email.find("@")]

        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, first_name=None, last_name=None, university_name=None, phone_number=None, home_address=None, about_user=None):
        user = self.create_user(email, password=password,
                                first_name=first_name, last_name=last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    first_name = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    university_name = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )
    home_address = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    about_user = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    user_type = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True,)
    is_admin = models.BooleanField(default=False,)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):  # Python 3
        return self.email

    def __unicode__(self):           # Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

#     def new_user_reciever(sender, instance, created, *args, **kwargs):
#     	if created:

# Going to use signals to send emails
# post_save.connect(new_user_reciever, sender=MyUser)


class Student(models.Model):
    user = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True)

    experience = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    languages = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )

    def get_full_name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    def get_short_name(self):
        return self.user.first_name

    def __str__(self):  # Python 3
        return self.user.email

    def __unicode__(self):           # Python 2
        return self.user.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return False

class Bookmark(models.Model):
    userID = models.IntegerField(null=True, blank=True)
    projectID = models.IntegerField(null=True, blank=True)


class Teacher(models.Model):
    user = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True)
    photo = '0';

    def get_full_name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    def get_short_name(self):
        return self.user.first_name

    def __str__(self):  # Python 3
        return self.user.email

    def __unicode__(self):           # Python 2
        return self.user.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True

class Engineer(models.Model):
    user = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True)

    def get_full_name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    def get_short_name(self):
        return self.user.first_name

    def __str__(self):  # Python 3
        return self.user.email

    def __unicode__(self):           # Python 2
        return self.user.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        #is engineer type-staff or type-engineer?
        return True
