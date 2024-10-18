from django.shortcuts import render
from .Products import Product  # Importing Product model from models.py

def home(request):
    products = Product.objects.all()  # Fetching all Product instances and storing in 'products'
    return render(request, 'index.html', {'products': products})  # Passing 'products' to the template
