from django.forms import ModelForm
from .models import Teacher, Class, Subject, Students, Result
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'




class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')