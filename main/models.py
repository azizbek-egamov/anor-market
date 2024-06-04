from django.db import models

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.first_name}"
    
class Book(models.Model):
    name = models.CharField(max_length=255)
    avtor = models.CharField(max_length=255)
    narx = models.IntegerField()
    rasm = models.FileField(upload_to='photo')
    
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Products(models.Model):
    # category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    name = models.TextField()
    info = models.TextField()
    narx = models.IntegerField()
    soni = models.IntegerField()
    rasm = models.FileField(upload_to='photo')
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Orders(models.Model):
    category = models.CharField(max_length=200)
    product_id = models.IntegerField()
    username = models.TextField()
    name = models.TextField()
    info = models.TextField()
    narx = models.IntegerField()
    soni = models.IntegerField()
    rasm = models.FileField(upload_to='photo')
    viloyat = models.TextField()
    holat = models.TextField()
    
    
        