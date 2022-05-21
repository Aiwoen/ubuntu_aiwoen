from django.db import models


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegeField(default=1)
    
# Create your models here.
