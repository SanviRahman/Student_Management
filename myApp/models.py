from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    subject=models.CharField(max_length=100)
    phone=models.CharField(max_length=15,blank=True,null=True)
    address=models.TextField(max_length=200,blank=True,null=True)
   

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    marks = models.IntegerField()
    grade = models.CharField(max_length=10)
    total_marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name}"
