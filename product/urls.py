from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('<int:product_id>', views.single_product, name="single")
]