"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from details.views import add_teacher_view, edit_teacher_view, delete_teacher_view, add_class_view, edit_class_view, class_pdf_view
from details.views import delete_class_view, add_student_view, edit_student_view, delete_student_view, teacher_pdf_view
from details.views import add_subject_view, edit_subject_view, delete_subject_view, home_view, student_pdf_view
from details.views import login_view, sign_up_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign_up/', sign_up_view, name="sign_up_page"),
    path('', home_view, name="home_page"),

    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    
    path('add_teacher/', add_teacher_view, name="add_teacher_page"),
    path('edit_teacher/<int:teacher_id>/', edit_teacher_view, name="edit_teacher_page"),
    path('delete_teacher/<int:teacher_id>/', delete_teacher_view, name="delete_teacher_page"),
    path('teacher_pdf/', teacher_pdf_view, name="teacher_pdf_page"),

    path('add_class/', add_class_view, name="add_class_page"),
    path('edit_class/<int:class_id>/', edit_class_view, name="edit_class_page"),
    path('delete_class/<int:class_id>/', delete_class_view, name="delete_class_page"),
    path('class_pdf/', class_pdf_view, name="class_pdf_page"),

    path('add_student/', add_student_view, name="add_student_page"),
    path('edit_student/<int:students_id>/', edit_student_view, name="edit_student_page"),
    path('delete_student/<int:students_id>/', delete_student_view, name="delete_student_page"),
    path('student_pdf/', student_pdf_view, name="students_pdf_page"),

    path('add_subject/', add_subject_view, name="add_subject_page"),
    path('edit_subject/<int:subject_id>/', edit_subject_view, name="edit_subject_page"),
    path('delete_subject/<int:subject_id>/', delete_subject_view, name="delete_subject_page"),
]