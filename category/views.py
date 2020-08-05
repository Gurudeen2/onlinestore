from django.shortcuts import render
from product.models import Product

def categ(request):
    catego = Product.objects.order_by('-prod_date')
    return render(request, 'product/categories.html')