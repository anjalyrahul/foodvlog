
from django.shortcuts import redirect, render,get_object_or_404
from iceapp.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_details(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active)
        for i in ct_items:
            tot +=(i.product.price*i.quan)
            count +=i.quan
    except ObjectDoesNotExist:
            pass
    return render(request,'cart.html',{'ct':ct_items})



def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    product=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(product=product,cart=ct)
    if c_items.quan>1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart_details')

def cart_delete(request,pr):
    ct=cartlist.objects.get(cart_id=c_id(request))
    product=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(product=product,cart=ct)
    c_items.delete()
    return redirect('cart_details')

