from django.db import models

# Create your models here.

class Register(models.Model):
    full_name = models.CharField(max_length=18)
    email = models.EmailField()
    password = models.CharField(max_length=12)


class Feedback(models.Model):
    email = models.EmailField()
    feedback = models.CharField(max_length=150)

class Billing_details(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    email = models.EmailField()
    phone = models.BigIntegerField()
    street_address = models.CharField(max_length=200)
    apartment_address = models.CharField(max_length=60)
    city = models.CharField(max_length=18)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    postcode = models.BigIntegerField()
