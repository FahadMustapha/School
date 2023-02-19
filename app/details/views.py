from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import render_to_pdf
from .form import TeacherForm, ClassForm, StudentsForm, SubjectForm,LoginForm, SignUpForm
from .models import Teacher, Class, Students, Subject
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required
def home_view(request):
    return render(request, 'home.html')

#TeacherForm
@login_required
def add_teacher_view(request):
    message =""
    if request.method == "POST":
        teacher_form = TeacherForm(request.POST)
        if teacher_form.is_valid():
            teacher_form.save()
            message="Teacher Added Successfully"
            
    else:
        teacher_form = TeacherForm()

    messages.success(request, message)    

    teachers = Teacher.objects.all()

    context ={
        'form':teacher_form,
        'msg':message,
        'teachers':teachers, 
    }
    return render(request, "add_teacher.html", context)

def teacher_pdf_view(request):
    teachers = Teacher.objects.all()

    context = {
        'teacher': teachers
    }
    return render_to_pdf("teacher_pdf.html", context)


@login_required
def edit_teacher_view(request, teacher_id):
    message =""
    teacher = Teacher.objects.get(id=teacher_id)

    if request.method == "POST":
        teacher_form = TeacherForm(request.POST, instance= teacher)

        if teacher_form.is_valid():
            teacher_form.save()
            message = "Changes saved successfully"
        else:
            message = "Entered invalid data"
        messages.success(request, message)

    else:
        teacher_form = TeacherForm(instance=teacher)
    
    context = {
        'form': teacher_form,
        'teacher': teacher,
        'msg': message,        
    }
    return render(request, "edit_teacher.html", context)

@login_required
def delete_teacher_view(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)

    teacher.delete()
    message = "Deleted"
    return redirect(add_teacher_view)

#Class Form
@login_required
def add_class_view(request):
    message =""
    if request.method == "POST":
        class_form = ClassForm(request.POST)
        if class_form.is_valid():
            class_form.save()
            message="Class Added Successfully"
        else:
            message="Invalid details"
        messages.success(request, message)

    else:
        class_form = ClassForm()

    classes = Class.objects.all()

    context ={
        'form':class_form,
        'msg':message,
        'class':classes,
    }
    return render(request, "add_class.html", context)
    
def class_pdf_view(request):
    classes = Class.objects.all()

    context ={
        'class': classes
    }
    return render_to_pdf("class_pdf.html", context)

@login_required
def edit_class_view(request, class_id):
    message = ''
    classes = Class.objects.get(id=class_id)

    if request.method == "POST":
        class_form = ClassForm(request.POST, instance= classes)

        if class_form.is_valid():
            class_form.save()
            message = "Changes saved successfully"
        else:
            message = "Entered invalid data"
        messages.success(request, message)
    else:
        class_form = ClassForm(instance=classes)
    
    context = {
        'form': class_form,
        'class': classes,
        'msg': message,        
    }
    return render(request, "edit_class.html", context)

@login_required
def delete_class_view(request, class_id):
    message = ""
    classes = Class.objects.get(id= class_id)

    classes.delete()
    message = "Deleted"
    return redirect(add_class_view)

#Student's Form
@login_required
def add_student_view(request):
    message = ""
    if request.method == "POST":
        students_form = StudentsForm(request.POST)
        if students_form.is_valid():
            students_form.save()
            message = "Student Added"
        else:
            message = "Details don't match"
        messages.success(request, message)

    else:
        students_form = StudentsForm()

    students = Students.objects.all()
    context = {
        'form':students_form,
        'msg':message,
        'student':students
    }
    return render(request, "add_students.html", context)

def student_pdf_view(request):
    students = Students.objects.all()

    context = {
        'student': students
    }
    pdf = render_to_pdf("students_pdf.html", context)

    return HttpResponse(pdf, content_type = "application/pdf")

@login_required
def edit_student_view(request, students_id):

    message = ''
    students = Students.objects.get(id= students_id)

    if request.method == "POST":
        students_form = StudentsForm(request.POST, instance= students)

        if students_form.is_valid():
            students_form.save()
            message = "Changes saved successfully"
        else:
            message = "Entered invalid data"
        messages.success(request, message)

    else:
        students_form = StudentsForm(instance=students)
    
    context = {
        'form': students_form,
        'student': students,
        'msg': message,        
    }
    return render(request, "edit_student.html", context)

@login_required
def delete_student_view(request, students_id):
    message = ""
    students = Students.objects.get(id = students_id)

    students.delete()
    message = "Student Deleted successfully"
    return redirect(add_student_view)

#subject Form.
@login_required
def add_subject_view(request):
    message = ""
    if request.method == "POST":
        subeject_form = SubjectForm(request.POST)

        if subeject_form.is_valid():
            subeject_form.save()
            message = "Sublect Successfully Added"
        else:
            message = "Invalid details provided"
        messages.success(request, message)

    else:
        subeject_form = SubjectForm()
    subjects = Subject.objects.all()

    context = {
        'form': subeject_form,
        'msg': message,
        'subjects':subjects
    }
    return render(request, 'add_subject.html', context)

@login_required
def edit_subject_view(request, subject_id):
    message = ''
    subject = Subject.objects.get(id= subject_id)

    if request.method == "POST":
        subject_form = SubjectForm(request.POST, instance= subject)

        if subject_form.is_valid():
            subject_form.save()
            message = "Changes saved successfully"
        else:
            message = "Entered invalid data"
        messages.success(request, message)        

    else:
        subject_form = SubjectForm(instance=subject)
    
    context = {
        'form': subject_form,
        'subjects': subject,
        'msg': message,        
    }
    return render(request, "edit_subject.html", context)

@login_required
def delete_subject_view(request, subject_id):
    message = ""
    subject = Subject.objects.get(id = subject_id)

    subject.delete()
    message = "Subject deleted"
    return redirect(add_subject_view)

def sign_up_view(request):
    message = ""
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            message = "User created successfully"
            success = True
            return redirect("accounts/login.html")
            
        else:
            message = "Invalid Inputs"
        messages.success(request, message)

    else:
        sign_up_form = UserCreationForm()
    context = {
        'form': sign_up_form
    }
    return render(request, 'registration/register.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "registration/login.html", {"form": form, "msg": msg})


def register_user_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            #return redirect("accounts/login.html")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "./register.html", {"form": form, "msg": msg, "success": success})