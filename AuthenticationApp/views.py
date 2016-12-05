"""AuthenticationApp Views"""

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages


from .forms import LoginForm, UpdateForm, RegisterFormStu, RegisterFormTeach, RegisterFormEngineer
from .models import MyUser, Student, Teacher, Engineer

# Auth Views

def select_usertype(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    return render(request, 'select_usertype.html')

def getProfiles(request):
    if request.user.is_authenticated():
        profiles_list = MyUser.objects.all()
        context = {
            'profiles' : profiles_list,
        }
        return render(request, 'profiles.html', context)

    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getProfile(request):
    if request.user.is_authenticated():
        in_email = request.GET.get('email', 'None')
        this_user = MyUser.objects.get(email__exact=in_email)

        context = {
            'profile' : this_user,
        }

        if (this_user.user_type == "PROF"):
            return render(request, 'teacherProfile.html', context)

        elif (this_user.user_type == "ENG"):
            return render(request, 'engineerProfile.html', context)
        else: # Student
            this_student = Student.objects.get(user_id__exact=this_user.id)

            context = {
                'profile': this_user,
                'student': this_student,
            }
            return render(request, 'studentProfile.html', context)

    # render error page if user is not logged in
    return render(request, 'autherror.html')

def auth_login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if next_url is None:
        next_url = "/"
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            messages.success(request, 'Success! Welcome, ' +
                             (user.first_name or ""))
            login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            messages.warning(request, 'Invalid username or password.')

    context = {
        "form": form,
        "page_name": "Login",
        "button_value": "Login",
        "links": ["register"],
    }
    return render(request, 'auth_form.html', context)


def auth_logout(request):
    logout(request)
    messages.success(request, 'Success, you are now logged out')
    return render(request, 'index.html')

def auth_register_engineer(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    form = RegisterFormEngineer(request.POST or None)

    if form.is_valid():
        new_user = MyUser.objects.create_user(email=form.cleaned_data['email'],
                                              password=form.cleaned_data[
                                                  "password2"],
                                              first_name=form.cleaned_data['firstname'], last_name=form.cleaned_data['lastname'],
                                              user_type='ENG', university_name=form.cleaned_data['universityname'],
                                              phone_number=form.cleaned_data['phonenumber'], home_address=form.cleaned_data['homeaddress'],
                                              about_user=form.cleaned_data['aboutuser']
                                              )
        new_user.save()

        # Register Engineer
        new_engineer = Engineer(user=new_user)
        new_engineer.save()

        login(request, new_user)
        messages.success(request, 'Success! Your account was created.')
        return render(request, 'index.html')

    context = {
        "form": form,
        "page_name": "Register",
        "button_value": "Register",
        "links": ["login"],
    }
    return render(request, 'auth_form.html', context)

def auth_register_teacher(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    form = RegisterFormTeach(request.POST or None)

    if form.is_valid():

        new_user = MyUser.objects.create_user(email=form.cleaned_data['email'],
                                              password=form.cleaned_data[
                                                  "password2"],
                                              first_name=form.cleaned_data['firstname'], last_name=form.cleaned_data['lastname'],
                                              user_type='PROF', university_name=form.cleaned_data['universityname'],
                                              phone_number=form.cleaned_data['phonenumber'], home_address=form.cleaned_data['homeaddress'],
                                              about_user=form.cleaned_data['aboutuser']
                                              )
        new_user.save()

        # Register teacher
        new_teacher = Teacher(user=new_user)
        new_teacher.save()

        login(request, new_user)
        messages.success(request, 'Success! Your account was created.')
        return render(request, 'index.html')

    context = {
        "form": form,
        "page_name": "Register",
        "button_value": "Register",
        "links": ["login"],
    }
    return render(request, 'auth_form.html', context)


def auth_register_student(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    form = RegisterFormStu(request.POST or None)

    if form.is_valid():
        new_user = MyUser.objects.create_user(email=form.cleaned_data['email'],
                                              password=form.cleaned_data[
                                                  "password2"],
                                              first_name=form.cleaned_data['firstname'], last_name=form.cleaned_data['lastname'],
                                              user_type='STU', university_name=form.cleaned_data['universityname'],
                                              about_user=form.cleaned_data['aboutuser'],
                                              home_address=form.cleaned_data['homeaddress'],
                                              phone_number=form.cleaned_data['phonenumber']
                                              )
        new_user.save()
        # Also registering students
        new_student = Student(user=new_user)
        new_student.languages = form.cleaned_data['languages']
        new_student.experience = form.cleaned_data['yearsExperiance']
        new_student.save()

        login(request, new_user)
        messages.success(request, 'Success! Your account was created.')
        return render(request, 'index.html')

    context = {
        "form": form,
        "page_name": "Register",
        "button_value": "Register",
        "links": ["login"],
    }
    return render(request, 'auth_form.html', context)


@login_required
def update_profile(request):
    form = UpdateForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Success, your profile was saved!')

    context = {
        "form": form,
        "page_name": "Update",
        "button_value": "Update",
        "links": ["logout"],
    }
    return render(request, 'auth_form.html', context)
