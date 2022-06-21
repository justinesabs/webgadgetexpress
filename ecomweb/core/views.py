import email
import imp
from itertools import product
import re
from unicodedata import category, name
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from product.models import Product, Category

from .forms import SignUpForm
from .models import Carausel


def frontpage(request):
    products = Product.objects.all()[0:2]
    return render(request, 'core/frontpage.html', {'products': products})
"""
def frontpage(request):
    obj = Carausel.objects.all()
    context ={
        'obj':obj
    }
    return render(request, 'core/frontpage.html', context)
"""
def aboutus(request):
    return render(request, 'core/aboutus.html')

def testing(request):
    return render(request, 'core/testing.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')

    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }
    return render(request, 'core/shop.html', context)
