from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def home(request,c_slug=None):
    c_page=None
    product=None
    if c_page!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        product=products.objects.filter(category=c_page,available=True)
    else:
        product=products.objects.all().filter(available=True)
    ct=categ.objects.all()
    paginator=Paginator(product,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
   
    return render(request,'index.html',{'pr':product,'ct':ct,'pg':pro})

def prodDetails(request,c_slug,product_slug):
    try:
        product=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception:
        return render(request,'product.html',{'pr':product})

def searching(request):
    return render(request,'search.html')

