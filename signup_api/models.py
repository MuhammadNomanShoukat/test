from django.db import models
from django.contrib.auth.models import AbstractUser



# ===================================== AbstractUser User model class declaring here ==============================
class SignUpModel(AbstractUser):
    semester = models.CharField(max_length=200,default="",verbose_name="user-semester")
    cgpa = models.FloatField(default=0.0)
    uni = models.CharField(max_length=200,default="Lahore University",verbose_name="University")
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=200,default="",verbose_name="Address")