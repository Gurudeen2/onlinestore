from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator


def product(request):
    product = Product.objects.order_by('-prod_date')
    nav = Product.objects.all()

    paginator = Paginator(product, 10)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    context = {
        'get_products': paged_product,
        'category': nav
    }

    return render(request,'product/product.html', context)

def single_product(request, product_id):
    single = get_object_or_404(Product, pk=product_id)
    nav = Product.objects.all()

    context = {
        'single': single,
        'category': nav
    }


    return render(request,'product/single_product.html', context)
 # start with products