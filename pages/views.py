from django.shortcuts import render
from product.models import Product

def index(request):
    product = Product.objects.order_by('-prod_date').filter(sticky=True)[:6]
    recent = Product.objects.order_by('-prod_date')[:6]
    context = {
        'products': product,
        'recent': recent,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    
    return render(request, 'pages/contact.html')
