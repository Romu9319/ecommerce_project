
from django.urls import path
from . import views

app_name = "web"
urlpatterns = [
    path('',views.index, name="index"),
    path("productsByCategory/<int:category_id>", views.productsByCategory, name="productsByCategory"),
    path("productsByName", views.productsByName, name="productsByName"),
    path("product/<int:product_id>", views.productDetail, name="product"),
    path("car", views.car, name="car"),
    path("addToCar/<int:product_id>", views.addToCar, name="addToCar"),
    path("deleteProductToCar/<int:product_id>", views.deleteProductToCar, name="deleteProductToCar"),
    path("clearCar", views.clearCar, name="clearCar")
]
