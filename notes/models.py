# Create your models here.
from django.db import models
from django.contrib.auth.models import Permission, User


class Note(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)