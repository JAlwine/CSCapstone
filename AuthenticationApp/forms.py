"""AuthenticationApp Forms"""

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import MyUser


class LoginForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    USER_TYPES = (
        ('STU', 'Student'),
        ('TEACH', 'Teacher'),
        ('ENG', 'Engineer')
    )

    """A form to creating new users. Includes all the required
    fields, plus a repeated password."""

    email = forms.CharField(
        label='Email', widget=forms.EmailInput, required=True)
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput, required=True)

    firstname = forms.CharField(
        label="First name", widget=forms.TextInput, required=False)
    lastname = forms.CharField(
        label="Last name", widget=forms.TextInput, required=False)
    universityname = forms.CharField(
        label="University", widget=forms.TextInput, required=False)
    phonenumber = forms.CharField(
        label="Phone number", widget=forms.TextInput, required=False)
    homeaddress = forms.CharField(
        label="Home address", widget=forms.TextInput, required=False)
    aboutuser=forms.CharField(
        label="About user", widget=forms.Textarea, required=False)

    # Add field for selecting type of user (Student, Teacher, ...)
    user_type = forms.ChoiceField(choices=USER_TYPES, required=True)


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Check if email exists before
        try:
            exists = MyUser.objects.get(email=email)
            raise forms.ValidationError("This email has already been taken")
        except MyUser.DoesNotExist:
            return email
        except:
            raise forms.ValidationError(
                "There was an error, please contact us later")


class UpdateForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'user_type', 'first_name', 'last_name', 'university_name', 'phone_number', 'home_address', 'about_user')
        widgets = { 'about_user':forms.Textarea(), 'user_type':forms.TextInput(attrs={'readonly': 'readonly'})}

    def clean_password(self):
        return self.initial["password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Check is email has changed
        if email == self.initial["email"]:
            return email
        # Check if email exists before
        try:
            exists = MyUser.objects.get(email=email)
            raise forms.ValidationError("This email has already been taken")
        except MyUser.DoesNotExist:
            return email
        except:
            raise forms.ValidationError(
                "There was an error, please contact us later")

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        # Check is email has changed
        if first_name is None or first_name == "" or first_name == '':
            email = self.cleaned_data.get("email")
            return email[:email.find("@")]
        return first_name


"""Admin Forms"""


class AdminUserCreationForm(forms.ModelForm):
    """A form for Admin to creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'user_type','last_name', 'university_name', 'home_address', 'about_user','phone_number')
        widgets = {'about_user': forms.Textarea()}

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AdminUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for Admin for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'first_name',
                  'last_name', 'user_type', 'university_name', 'phone_number', 'home_address','about_user', 'is_active', 'is_admin')#is_staff  ??
        widgets = {'about_user': forms.Textarea()}

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
