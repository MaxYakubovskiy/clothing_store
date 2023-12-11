from django.urls import path, include
from product.views import MainShop

app_name = 'product'

urlpatterns = [
    path('', MainShop.as_view(), name='mainshop'),
]