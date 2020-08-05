from django.shortcuts import render, redirect
from .models import Cart
from django.contrib import messages
from product.models import Product


def cart(request):
    if request.method ==  'POST':
        name = request.POST['name']
        idd = request.POST['prod_id']
        username = request.POST['username']
        #check if cart already existed
        if request.user.is_authenticated:
            has_cart = Cart.objects.all().filter(idd=idd, username=username)
            if has_cart:
                messages.error(request, 'Cart Already Existed')
                return redirect('cart')
        cart = Cart(name=name, idd=idd, username=username)
        cart.save()

    dash = Cart.objects.order_by('-cart_date').filter(username=request.user.username)
    # paginator = Paginator(dash, 10)
    # page = request.GET.get('cart')
    # dash_page = paginator.get_page(page)
    nav = Product.objects.all()

    context ={
        'dash': dash,
        'category': nav
    }
    return render(request, 'account/cart.html', context)

