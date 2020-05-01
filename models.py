from django.db import models

# Create your models here.
class Registration(models.Model):
    emailid = models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.emailid
class Registration1(models.Model):
    emailid=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.emailid
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
class Questions(models.Model):
    subname=models.CharField(max_length=50)
    marks=models.CharField(max_length=10)
    question=models.CharField(max_length=500)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    def __str__(self):
        return self.subname
class Enrollment(models.Model):
    subjectname=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    def __str__(self):
        return self.emailid
class Marks(models.Model):
    emailid=models.CharField(max_length=50)
    subname=models.CharField(max_length=50)
    marksvalue=models.CharField(max_length=10)
    marks=models.CharField(max_length=10)
    def __str__(self):
        return self.emailid



