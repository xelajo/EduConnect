from django.db import models

# Create your models here.
class Teacher(models.Model):
    photo=models.FileField(max_length=100)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.IntegerField()
    qualification=models.CharField(max_length=100)
    experience=models.IntegerField()
    contactno=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100,default="teacher")
class Student(models.Model):
    photo=models.FileField(max_length=100)
    admno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.DateField(null=True)
    parentname=models.CharField(max_length=100)
    relationship=models.CharField(max_length=100)
    contactno=models.IntegerField()
    department=models.CharField(max_length=100)
    semester=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100,default="student")

class Parent(models.Model):
    parentname=models.CharField(max_length=100)
    studadmno=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    gender=models.CharField(max_length=100)
    contactno=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100,default="parent")
class Login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100)
class Notification(models.Model):
    notification_id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    teacherid=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    department=models.CharField(max_length=100)
    semester=models.CharField(max_length=100)
    notification=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
class Noteupload(models.Model):
    noteupload_id=models.AutoField(primary_key=True)
    teacherid=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    subject=models.CharField(max_length=100)
    topic=models.CharField(max_length=100)
    uploadnotes=models.FileField(max_length=100)
    department=models.CharField(max_length=100)
    semester=models.CharField(max_length=100)
class notificationparent(models.Model):
    notification_id=models.AutoField(primary_key=True)
    teacherid=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    studentid=models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    currentdate=models.DateField(auto_now_add=True,null=True)
    notification=models.CharField(max_length=100)




