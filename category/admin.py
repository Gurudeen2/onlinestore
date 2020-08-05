from django.contrib import admin
from .models import cate

class AdminCart(admin.ModelAdmin):
    list_display= ('id', 'cate_name')
    list_display_links = ('id', 'cate_name')
    search_fields = ('cate_name',)
    list_filter = ('cate_name',)
    list_per_page = 20

admin.site.register(cate, AdminCart)