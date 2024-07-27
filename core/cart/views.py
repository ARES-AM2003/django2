from django.shortcuts import render
from .models import Cart
# Create your views here.
def cart(request):
    carts = Cart.objects.all()
    context = {'carts':carts}
    return render(request, 'cart/cart.html', context)
