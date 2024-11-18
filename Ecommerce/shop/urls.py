"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
app_name="shop"

urlpatterns = [
    path('',views.categories,name="categories"),
    path('products/<int:p>',views.products,name="products"),
    path('details/<int:p>',views.details,name="details"),
    path('register',views.register,name="user_register"),
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('addcategory',views.add_category,name="add_category"),
    path('addproduct',views.add_product,name="add_product"),
    path('addstock/<int:pr>',views.add_stock,name="add_stock"),
    path('edit/<int:i>',views.edit,name="edit"),
    path('delete/<int:i>',views.delete,name="delete"),

]
