from django.db import models

# Create your models here.

class Domain(models.Model):
     D_name=models.CharField(max_length=100)
     D_desc=models.TextField()

