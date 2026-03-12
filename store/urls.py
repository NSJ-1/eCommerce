from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get/stores/', views.view_stores),
    path('add/store/', views.add_store),
    path('get/products/', views.view_products),
    path('add/product/', views.add_product),
    path('external/products/', views.external_products),
]
