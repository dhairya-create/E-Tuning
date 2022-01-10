from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from datetime import datetime
from home.models import Sell,Cart,Order,Contact,Register,Product,Category
from django.contrib import messages
from django.views import View
from home.middlewares.auth import auth_middleware
from home.middlewares.artist_auth import artist_auth_middleware
from django.utils.decorators import method_decorator

class Cart(View):
    @method_decorator(auth_middleware)
    @method_decorator(artist_auth_middleware)
    def get(self,request):
        ids = list(request.session['cart'].keys())
        products = Product.get_products_by_id(ids)        
        return render(request, 'cart.html',{'products': products})

    def post(self,request):
        id = request.POST.get('remove')
        cart = request.session.get('cart')
        print(cart)
        if id:
            cart.pop(id)
        request.session['cart'] = cart
        return redirect('/cart')        
