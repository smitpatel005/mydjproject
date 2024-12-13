from django.db import models

class student(models.Model):
    studentname=models.CharField("name",max_length=50,blank=False)
    studentnumber=models.IntegerField("moblie")
    studentemail=models.CharField("Email",max_length=50)
    studentpassword=models.CharField("password",max_length=50)
    createdAT=models.DateTimeField("created",auto_now_add=True)



    def __str__(self):
        return self.studentname
    
