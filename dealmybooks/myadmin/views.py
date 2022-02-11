from unicodedata import category
from django.shortcuts import render, redirect
from user.models import *
from myadmin.models import *

def dashboard(request):
	return render(request, "myadmin/home.html")

def login(request):
	return render(request, "myadmin/login.html")


# Users
def user(request):
	return render(request, "myadmin/user.html", {"rows" : Register.objects.all()})

def delete_user(request, id):
	Register.objects.get(id=id).delete()
	return redirect("/myadmin/user/")


# Categories	
def Add_category(request):	
	return render(request, "myadmin/add_category.html")

def post_category(request):
	AddCategory.objects.create(category=request.POST['category'])
	return redirect("/myadmin/add_category/")

def all_category(request):
	return render(request, "myadmin/all_category.html", {"categories" : AddCategory.objects.all()})

def update_category(request, id):
	update_item = AddCategory.objects.get(id=id)
	context = {"update_item" : update_item}
	return render(request, "myadmin/update_category.html", context)

def updated_category(request, id):
	updated_item = request.POST['category']
	AddCategory.objects.update_or_create(id=id, defaults={"category" : updated_item})
	return redirect("/myadmin/all_category/")

def delete_category(request, id):
	AddCategory.objects.get(id=id).delete()
	return redirect("/myadmin/all_category/")


# Subcategory
def Subcategory(request):
	return render(request, "myadmin/add_subcategory.html", {"categories": AddCategory.objects.all()})

def insert_subcategory(request):
	AddSubCategory.objects.create( category=request.POST['category'], subcategory=request.POST['subcategory'])
	return redirect("/myadmin/add_subcategory/")

def all_subcategory(request):
	return render(request, "myadmin/all_subcategory.html",{"scates": AddSubCategory.objects.all()})

def update_subcategory(request, id):
	categories = AddCategory.objects.all()
	subcategories = AddSubCategory.objects.get(id=id)
	context = {"subcategories": subcategories, "categories": categories}
	return render(request, "myadmin/update_subcategory.html", context)

def updated_subcategory(request, id):
	AddSubCategory.objects.update_or_create(id=id, defaults = {"category": request.POST['category'], "subcategory": request.POST['subcategory']})
	return redirect("/myadmin/all_subcategory/")

def delete_subcategory(request, id):
	AddSubCategory.objects.get(id=id).delete()
	return redirect("/myadmin/all_subcategory/")


# Orders
def orders(request):
	return render(request, "myadmin/orders.html")

# Feedback
def feedback(request):
	return render(request, "myadmin/feedback.html", { "feedbacks": Feedback.objects.all() })
	
# Logout
def logout(request):
	return redirect("/myadmin/")





