from django.db import models
from django.db import models
from django.db.models.fields import CharField
# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=10)

