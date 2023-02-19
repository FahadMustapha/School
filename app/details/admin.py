from django.contrib import admin
from .models import Teacher,  Class, Subject, Students, Result

# Register your models here.

class teacherAdmin(admin.ModelAdmin):
    list_display = ("Teacher_name", "Gender", "Address", "Contact")

admin.site.register(Teacher, teacherAdmin)


class ClassAdmin(admin.ModelAdmin):
    list_display = ("Class_name", "Class_Teacher", "Class_fees")
    
admin.site.register(Class, ClassAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("Subject_name",)

admin.site.register(Subject, SubjectAdmin)


class StudentsAdmin(admin.ModelAdmin):
    list_display = ("Student_name", "Class_Id", "Gender", "Address", "Guardian", "Guardian_Contact")

admin.site.register(Students, StudentsAdmin)


class ResultAdmin(admin.ModelAdmin):
    list_display = ("Results_date", "Class_Id", "Student_Id", "Subject_Id", "Score", "Grades", "Teacher_Id")

admin.site.register(Result, ResultAdmin)