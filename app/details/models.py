from django.db import models

# Create your models here.
class Teacher(models.Model):
    Gender_Choices=[
        ("M", "Male"),
        ("F", "Female")
    ]
    Teacher_name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=2, choices=Gender_Choices )
    Address = models.CharField(max_length=10)
    Contact = models.CharField(max_length=10)
    def __str__(self):
        return self.Teacher_name

class Class(models.Model):
    Class_name = models.CharField(max_length=50)
    Class_Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Class_fees = models.IntegerField()
    def __str__(self):
        return self.Class_name

    
class Subject(models.Model):
    Subject_name = models.CharField(max_length=50)


class Students(models.Model):
    Gender_Choices=[
        ("M", "Male"),
        ("F", "Female")
    ]
    Student_name = models.CharField(max_length=50)
    Class_Id = models.ForeignKey(Class, on_delete=models.CASCADE)
    Gender = models.CharField(max_length=2, choices=Gender_Choices)
    Address = models.CharField(max_length=10)
    Guardian = models.CharField(max_length=10)
    Guardian_Contact = models.CharField(max_length=10)
    def __str__(self):
        return self.Class_Id

class Result(models.Model):
    Results_date = models.DateField(auto_now=False, auto_now_add=False)
    Class_Id = models.ForeignKey(Class, on_delete=models.CASCADE)
    Student_Id = models.ForeignKey(Students, on_delete=models.CASCADE)
    Subject_Id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Score = models.IntegerField(default=0)
    Grades = models.IntegerField(default=0)
    Teacher_Id = models.ForeignKey(Teacher, on_delete=models.CASCADE)