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
    

from django.contrib.auth.models import User

class Client(models.Model): 
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    dni = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, default="M")
    fhone = models.CharField(max_length=20)
    birthday_date = models.DateField(null=True)
    diection = models.TextField() 

    def __str__(self):
        return self.dni


class Order(models.Model):

    state_choices = (
        ("0", "required"),
        ("1", "paid")
    )

    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    singup_date = models.DateTimeField(auto_now_add=True)
    number_order= models.CharField(max_length=20, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    state = models.CharField(max_length=1, default="0", choices= state_choices)


    def __str__(self):
        return self.number_order
    

class DetailOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    cuantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name