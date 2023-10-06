from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    registration_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="products", blank=True)

    def __str__(self):
        return self.name
    
