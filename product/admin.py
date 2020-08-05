from django.contrib import admin
from .models import Product

class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'prod_name', 'category', 'price', 'sticky')
    list_display_links = ('id', 'prod_name', )
    list_filter =('prod_date',)
    list_editable = ('sticky', 'price',)
    search_fields = ('prod_name', 'price', 'category')
    list_per_page = 20

admin.site.register(Product, AdminProduct)
