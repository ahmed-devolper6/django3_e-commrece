from django.shortcuts import render
from products.models import Products
from .models import Cart , CartDeitl , Oders , OderDeitl , Coupon
from django.shortcuts import get_object_or_404
from django.utils.timezone import datetime
from django.template.loader import render_to_string
from django.http import JsonResponse
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
    cart = Cart.objects.get(user = request.user , status='inprogecss')
    delivery_cost = 15
    if request.method == 'POST':
        coupun = request.POST['coupon']
        coupon = get_object_or_404(Coupon , value=coupun)
        today = datetime.today().date()
        null_discount = 0
        
        if coupun and coupon.quantiity > 0:
            if today >= coupon.form_date and today <= coupon.to_date:
                discount = cart.get_total() / 100 * coupon.value
                total = cart.get_total() - discount +  delivery_cost
                discount = cart.get_total() / 100 * coupon.value
                html = render_to_string('include/summry.html', {"dev":delivery_cost , 'discount':discount , 'total':total , request:request})
                return JsonResponse({"resulat":html})

    return render(request,'oder/checkout.html',{})