from django.db import models
from django.contrib import admin
class student(models.Model):
    Stu_ID=models.CharField(max_length=20)
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField()

class studentAdmin(admin.ModelAdmin):
    list_display=('Stu_ID','Name','Department','Age','Email')