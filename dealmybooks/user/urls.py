"""dealmybooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from user import views
urlpatterns = [
    path('home/', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('user_register/', views.user_register, name='user_register'),
    path('cart/', views.cart, name='cart'),
    path('shop/', views.shop, name='shop'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('404/', views._404, name='404'),
    path('checkout/', views.checkout, name="checkout"),
    path('billing_details/', views.Billing_Details, name="billing_details"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('about/', views.about, name="about"),
    path('my_account/', views.my_account, name="my_account"),
    path('give_book/', views.give_book, name="give_book"),
    path('feedback/', views.feedback, name="feedback"),
    path('post_feedback/', views.post_feedback, name="feedback"),
    path('logout/', views.logout, name="logout"),
]
