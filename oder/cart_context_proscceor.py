from .models import Cart , CartDeitl
def user_cart(request):
    if request.user.is_authenticated:
        cart_user,created = Cart.objects.get_or_create(user = request.user , status='inprogecss')
        #cart_detil = CartDeitl.objects.get(cart = cart_user)
        return {'cart_user':cart_user}
    else:
        return {}

