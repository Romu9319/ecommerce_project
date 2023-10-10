from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .car import Car

# Create your views here.

def index(request):
    """VIEW FOR PRODUCTS CATALOG """
    product_list = Product.objects.all()
    category_list = Category.objects.all()

    context = {
        "products": product_list,
        "categories": category_list
    }
    return render(request, "index.html", context)


def productsByCategory(request, category_id):
    """VIEW FOR PRODUCTS BY CATEGORY """
    objCategory = Category.objects.get(pk=category_id)
    product_list = objCategory.product_set.all()
    category_list = Category.objects.all()

    context = {
        "categories": category_list,
        "products": product_list
    }
    
    return render(request, "index.html", context)


def productsByName(request):
    """VIEW FOR PRODUCTS BY NAME"""
    name = request.POST["name"]
    product_list = Product.objects.filter(name__contains = name)
    category_list = Category.objects.all()

    context = {
        "categories": category_list,
        "products": product_list
    }

    return render(request, "index.html", context)


def productDetail(request, product_id):
    """VIEW FOR PRODUCT DETAIL"""
    product = get_object_or_404(Product, pk=product_id) 
    context = {
        "product": product
    }
    return render(request, "product.html", context)


def car(request):
    return render(request, "car.html")


def addToCar(request, product_id):
    if request.method == "POST":
        cuantity = int(request.POST["cuantity"])
    else:
        cuantity = 1

    product = Product.objects.get(pk=product_id)
    carProduct = Car(request)
    carProduct.add(product, cuantity)

    if request.method == "GEt":
        return redirect("/")

    return render(request, "car.html")


def deleteProductToCar(request, product_id):
    product = Product.objects.get(pk=product_id)
    car = Car(request)
    car.delete(product)

    return render(request, "car.html")


def clearCar(request):
    car = Car(request)
    car.clear()

    return render(request, "car.html")