from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    
    def __str__(self):
        return self.name
    
