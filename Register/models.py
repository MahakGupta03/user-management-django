from django.db import models

# Create your models here.

class Register(models.Model):
    username = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    

