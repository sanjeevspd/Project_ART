from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table="admin_table"

    def __str__(self):
        return self.username
class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
