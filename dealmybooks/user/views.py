from turtle import st
from django.shortcuts import redirect, render
from user.models import *

# Create your views here.
def index(request):
    context = {}
    return render(request, "user/index.html", context)

def login(request):
    context = {}
    return render(request, "user/login.html", context)

def register(request):
    context = {}
    return render(request, "user/register.html", context)

def user_register(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    password = request.POST['password']
    Register.objects.create(    
                                full_name=full_name,
                                password=password,
                                email=email, 
    )
    return redirect("/user/register/")

def cart(request):
    context = {}
    return render(request, "user/cart.html", context)

def shop(request):
    context = {}
    return render(request, "user/shop.html", context)

def wishlist(request):
    context = {}
    return render(request, "user/wishlist.html", context)



def _404(request):
    context = {}
    return render(request, "user/404.html", context)

def checkout(request):
    context = {}
    return render(request, "user/checkout.html", context)

def Billing_Details(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone = request.POST['phone']
    street_address = request.POST['street_address']
    apartment_address = request.POST['apartment_address']
    apartment_address = request.POST['apartment_address']
    city = request.POST['city']
    state = request.POST['state']
    postcode = request.POST['postcode']
    Billing_details.objects.create(
                                first_name = first_name,
                                last_name = last_name,
                                email =email,
                                phone = phone,
                                street_address = street_address,
                                apartment_address = apartment_address,
                                city = city,
                                state = state,
                                postcode = postcode

    )
    return redirect("/user/checkout/")

def my_account(request):
    context = {}
    return render(request, "user/my_account.html", context)

def contact_us(request):
    context = {}
    return render(request, "user/contact.html", context)

def about(request):
    context = {}
    return render(request, "user/about.html", context)

def give_book(request):
    context = {}
    return render(request, "user/giveBook.html", context)

def feedback(request):
    context = {}
    return render(request, "user/feedback.html", context)

def post_feedback(request):
    email = request.POST['email']
    feedback = request.POST['feedback']
    Feedback.objects.create(email = email, feedback=feedback)

    return redirect("/user/feedback/")

def logout(request):
    """ Renders Logout Page. """
    context = {}
    return render(request, "user/login.html", context)