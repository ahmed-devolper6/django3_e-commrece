from django.shortcuts import render
from products.models import Products
from .models import Cart , CartDeitl , Oders , OderDeitl
# Create your views here.
def add_to_cart(request):
    if request.method == 'POST':
        proudct_id = request.POST['proudct_id']
        quantitiy = request.POST['quantity']
        proudct = Products.objects.get(id=proudct_id)
        cart = Cart.objects.get(user=request.user,status='inprogecss')
        cart_detil,created = CartDeitl.objects.get_or_create(
            cart = cart,
            proudct = proudct,
        )
        cart_detil.quantiity = quantitiy
        cart_detil.price = proudct.price
        cart_detil.total = int(quantitiy) * proudct.price
        cart_detil.save()
        
def oder_list(request):
    order = Oders.objects.filter(user=request.user)

    return render(request,'oder/orderlist.html',{'order':order})

def cheakout(request):
    
    return render(request,'oder/checkout.html',{})