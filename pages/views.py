from django.shortcuts import render
from django.http import HttpResponse
from products.models import *
from .models import *
from products.models import *
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def _navbar(request):

    return render ( request , 'partials/_navbar.html')

def index(request):
    cat = Category.objects.all()

    name = None
    desc = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            ser = ser.filter(name__icontains=name)
    context={
        'products':Product.objects.all(),
        'category':cat
    }
    return render ( request , 'pages/index.html', context )

def about(request):
    cat = Category.objects.all()
    context={
        'products':Product.objects.all(),
        'category':cat
    }

    return render ( request , 'pages/about.html', context )

def services(request):
    cat = Category.objects.all()

    name = None
    desc = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            ser = ser.filter(name__icontains=name)

    context = {
        'products':Product.objects.all(),
        'category':cat
    }
    return render ( request , 'pages/services.html', context )

def products(request):
    pro = Product.objects.all()
    cat = Category.objects.all()

    name = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            pro = pro.filter(description__icontains=name) | pro.filter(category__name__icontains=name) | pro.filter(name__icontains=name)

    if 'category' in request.GET:
        name = request.GET['category']
        if name:
            pro = pro.filter(category__name__icontains=name)
            
    paginator = Paginator(pro,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
            
    context = {
          'products':page_obj,
           page_obj:pro,
          'category':cat, 
   
    }
    return render(request,'products/products.html', context)

