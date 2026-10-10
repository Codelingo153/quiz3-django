from django.db import models

class Student(models.Model):
    StudentID = models.CharField(max_length=20, primary_key=True)
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Course = models.CharField(max_length=100)
    Section = models.CharField(max_length=10)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=15)

    def __str__(self):
        return self.Name
