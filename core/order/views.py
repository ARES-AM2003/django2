from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Order
from home.models import Products
from  django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    # This is the code that will be executed when the user clicks the submit button
    if request.method == 'POST':
        # fullName=request.POST.get('fullName')
        first_name=request.POST.get('first_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')

        if password!=password1:
            messages.error(request, 'Passwords do not match')
            return render(request, 'order/signup.html')
    
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'order/signup.html')
        user= User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.set_password( raw_password=password)
        
        user.save()
        messages.success(request, 'Account created successfully')   
        return render(request, 'order/login.html')


    return render(request, 'order/signup.html')

def Order(request):
    items = Products.objects.all()
    things_to_send= {'items':items}
    if request.method == 'POST':
        # fullName=request.POST.get('fullName')
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to place an order')
            return render(request, 'order/login.html')
        else:
            first_name=request.POST.get('first_name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            city=request.POST.get('city')
            state=request.POST.get('state')
            zip=request.POST.get('zip')
            notes=request.POST.get('notes')
            user=request.user
            order=Order(name=first_name, email=email, phone=phone, address=address, city=city, state=state, zip=zip, notes=notes, customer=user)
            order.save()
            messages.success(request, 'Order placed successfully')
            return render(request, 'order/order.html',things_to_send)
    return render(request, 'order/order.html',things_to_send)

def Login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            login( request,user)
            messages.success(request, 'Logged in successfully')
            return render(request, 'home/home.html')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'order/login.html')
    return render(request, 'order/login.html')