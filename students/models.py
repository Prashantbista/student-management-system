from django.db import models

# Create your models here.

class AIConversation(models.Model):    
 question = models.TextField()    
 answer = models.TextField()    
 created_at = models.DateTimeField(auto_now_add=True)    
 def __str__(self):        
  return self.question[:50]

 
class Course(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id} - {self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
            return f"{self.id} - {self.name}"


class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    address=models.CharField(max_length=200)
    course=models.ForeignKey(Course, on_delete=models.SET_NULL,null=True,blank=True, related_name="students")
    subjects=models.ManyToManyField(Subject, related_name="students")
    document= models.FileField(upload_to="documents/",blank=True)
    profile_picture= models.ImageField(upload_to="profile_pictures/", blank=True)


    def __str__(self):
        return f"{self.name} {self.age}"

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="profile")
    phone_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.age}"
