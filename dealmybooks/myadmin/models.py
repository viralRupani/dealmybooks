from django.db import models

# Create your models here.

class Login(models.Model):
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=8)

class AddCategory(models.Model):
	category = models.CharField(max_length=20)

class AddSubCategory(models.Model):
	category = models.CharField(max_length=20)
	subcategory = models.CharField(max_length=20)