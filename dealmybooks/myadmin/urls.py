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
from myadmin import views
urlpatterns = [
   path("", views.login, name="login"),
   path("dashboard/", views.dashboard, name="dashboard"),
   path("add_category/", views.Add_category, name="add_category"),
   path("post_category/", views.post_category, name="post_category"),
   path("add_subcategory/", views.Subcategory, name="add_subcategory"),
   path("addsubcategory/", views.insert_subcategory, name="insert_subcategory"),
   path("orders/", views.orders, name="orders"),
   path("user/", views.user, name="user"),
   path("delete_user/<int:id>", views.delete_user, name="delete_user"),
   path("all_category/", views.all_category, name="all_category"),
   path("update_category/<int:id>", views.update_category, name="update_category"),
   path("updated_category/<int:id>", views.updated_category, name="updated_category"),
   path("delete_category/<int:id>", views.delete_category, name="delete_category"), 
   path("all_subcategory/", views.all_subcategory, name="all_subcategory"),
   path("delete_subcategory/<int:id>", views.delete_subcategory, name="delete_subcategory"),
   path("update_subcategory/<int:id>", views.update_subcategory, name="update_subcategory"),
   path("updated_subcategory/<int:id>", views.updated_subcategory, name="updated_subcategory"),
   path("feedback/", views.feedback, name="feedback"),
   path("logout/", views.logout, name="logout"),
]
