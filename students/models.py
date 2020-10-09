from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    standard = models.CharField(max_length=5)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=256)
    class Meta:
        db_table = "student"