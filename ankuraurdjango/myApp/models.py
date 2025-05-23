from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()