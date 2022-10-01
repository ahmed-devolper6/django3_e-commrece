from django.shortcuts import render
from products.models import Products
from .models import Cart , CartDeitl
# Create your views here.
def add_to_cart(request):
    if request.method == 'POST':
        proudct_id = request.POST['proudct_id']
        quantitiy = request.POST['quantitiy']
        proudct = Products.objects.get(id = proudct_id)
        cart = Cart.objects.get(user = request.user , status = 'inprogecss')
        cart_detil,created = CartDeitl.objects.get_or_create(
            cart = cart,
            proudct = proudct,
        )
        cart_detil.quantiity = quantitiy
        cart_detil.price = proudct.price
        cart_detil.total = int(quantitiy) * proudct.price
        cart_detil.save()
        


