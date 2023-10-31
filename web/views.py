from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Category, Product, Client, Order, DetailOrder
from .car import Car
from paypal.standard.forms import PayPalPaymentsForm

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
    if request.method == 'POST':
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


"""Views for Clients and Users"""
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import ClientForm

def createUser(request):

    if request.method == 'POST':
        dataUser = request.POST.get("newUser")
        dataPassword = request.POST.get("newPassword")
        
        newUser = User.objects.create_user(username=dataUser, password=dataPassword)
        if newUser is not None:
            login(request, newUser)
            return redirect("/acount")    

    return render(request, "login.html")


def loginUser(request):
    landingPage = request.GET.get("next", None)
    context = {
        "destination": landingPage
    }

    if request.method == 'POST':
        dataUser = request.POST['user']
        dataPassword = request.POST['password']
        dataDestination = request.POST["destination"]

        userAuth = authenticate(request, username=dataUser, password=dataPassword)
        if userAuth is not None:
            login(request, userAuth)
            
            if dataDestination != "None":
                return redirect(dataDestination)
            
            return redirect("/acount")
        else: 
            context = {
                "error": "Incorrect data"
            }

    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return render(request, "login.html")


def userAcount(request):

    try:
        editClient = Client.objects.get(user = request.user)

        dataClient = {
            "name": request.user.first_name,
            "last name": request.user.last_name,
            "email": request.user.email,
            "address": editClient.address,
            "phone": editClient.phone,
            "dni": editClient.dni,
            "gender": editClient.gender,
            "birthdate": editClient.birthdate
        }
    except:
        dataClient = {
            "name": request.user.first_name,
            "last name": request.user.last_name,
            "email": request.user.email
            }

    clientForm = ClientForm(dataClient)
    context = {
        "clientForm": clientForm
    }

    return render(request, "cuenta.html", context)


def updateClient(request):
    menssage = ""

    if request.method == "POST":
        clientForm = ClientForm(request.POST)
        if clientForm.is_valid():
            dataClient = clientForm.cleaned_data
            # updating user
            updateUser = User.objects.get(pk=request.user.id)
            updateUser.first_name = dataClient["name"]
            updateUser.last_name =  dataClient["last_name"]
            updateUser.email = dataClient["email"]
            updateUser.save()
            # sing up client
            newClient = Client()
            newClient.user = updateUser
            newClient.dni = dataClient["dni"]
            newClient.address = dataClient["address"]
            newClient.phone = dataClient["phone"]
            newClient.gender = dataClient["gender"]
            newClient.birthdate = dataClient["birthdate"]
            newClient.save()

            menssage = "Data update"
    
    context = {
        "menssage": menssage,
        "clientForm": clientForm
    }


    return render(request, "cuenta.html", context)


    #Registrar Pedido
@login_required(login_url="/login")
def registerOrder(request):
    try:
        editClient = Client.objects.get(user = request.user)

        dataClient = {
            "name": request.user.first_name,
            "last name": request.user.last_name,
            "email": request.user.email,
            "address": editClient.address,
            "phone": editClient.phone,
            "dni": editClient.dni,
            "gender": editClient.gender,
            "birthdate": editClient.birthdate
        }
    except:
        dataClient = {
            "name": request.user.first_name,
            "last name": request.user.last_name,
            "email": request.user.email
            }

    clientForm = ClientForm(dataClient)
    context = {
        "clientForm": clientForm
    }

    return render(request, "pedido.html", context)

@login_required(login_url="/login")
def confirmOrder(request):
    context = {}
    if request.method == "POST":
            #actualizamos usuairo
        updateUser = User.objects.get(pk=request.user.id)
        updateUser.first_name = request.POST["name"]
        updateUser.last_name = request.POST["last_name"]
        updateUser.save()
        try:
            clientOrder = Client.objects.get(user=request.user)
            clientOrder.phone = request.POST["phone"]
            clientOrder.address = request.POST["address"]
            clientOrder.save()
        except:
            clientOrder = Client()
            clientOrder.user = updateUser
            clientOrder.phone = request.POST["phone"]
            clientOrder.address = request.POST["address"]
            clientOrder.save()
        # reguistramos nuevo pedido
        numberOrder = ""
        totalAmount = float(request.session.get("carTotal"))
        newOrder = Order()
        newOrder.client = clientOrder
        newOrder.save()

        # detalles del pedido
        orderCar = request.session.get("car")
        print("esto es order car", orderCar)
        for key,value in orderCar.items():
            productOrder = Product.objects.get(pk=value["product_id"])
            detail = DetailOrder()
            detail.order = newOrder
            detail.product = productOrder
            detail.cuantity = int(value["cuantity"])
            detail.subtotal = float(value["total"])
            detail.save()

        # actualizamos el pedido
        numberOrder = "ORDER" + newOrder.singup_date.strftime("%Y") + str(newOrder.id)
        newOrder.number_order = numberOrder
        newOrder.total = totalAmount
        newOrder.save()

        # Boton Paypal        
        paypal_dict = {
            "business": "sb-nntlf27846788@business.example.com",
            "amount": totalAmount,
            "item_name": "Order Code:" + numberOrder,
            "invoice": numberOrder,
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return": request.build_absolute_uri('/'),
            "cancel_return": request.build_absolute_uri('/logout')
        }

        # Create the instance.
        form = PayPalPaymentsForm(initial=paypal_dict)   

        context={
            "order": newOrder,
            "form": form
        }

        # limpiar carrito
        car = Car(request)
        car.clear()

    return render(request, "compra.html", context) 




