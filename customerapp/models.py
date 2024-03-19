from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Feedback(models.Model):
    name=models.CharField(max_length=200,blank=False)
    phone=models.CharField(max_length=12,blank=False,unique=True)
    email=models.EmailField(max_length=100,blank=False)
    feedback=models.CharField(max_length=1000,blank=False)
    class Meta:
        db_table="FeedBack"

    def __str__(self):
        return self.name

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.title


