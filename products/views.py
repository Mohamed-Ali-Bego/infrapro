from django.shortcuts import get_object_or_404, render
from datetime import datetime
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages



def products(request):
    pro = Product.objects.all()
    cat = Category.objects.all()

    name = None
    if 'searchname' in request.GET:
        name = request.GET.get('searchname', '').strip()
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






def product(request, pro_id):
    context = {
        'products':Product.objects.all(),
        'pro':get_object_or_404(Product, pk=pro_id)
    }
    return render(request,'products/product.html', context )