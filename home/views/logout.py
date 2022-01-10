from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError
from etuning.settings import EMAIL_HOST_USER
from home.models import Sell,Cart,Order,Contact,Register,Product,Artist2,Category
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
import re
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class Logout(View):
    def get(self,request):
        cart = request.session['cart']
        message = request.session['message']
        print(message)
        customer_id = request.session['customer']
        cart_item = Cart.get_cart_by_customer_id(customer_id)
        if cart_item:
            for i in cart_item:
                i.delete()    
        if cart:
            ids = list(request.session['cart'].keys())
            for j in ids:
                product = Product.objects.get(id=int(j))
                id = request.session['customer']
                customer = Register.objects.get(id= id)
                print(message.get(j))
                cart_add = Cart(customer = customer,
                product = product,
                quantity = int(cart.get(j)),
                message = message.get(j))
                print(cart_add)
                cart_add.save()
                    
        request.session.clear()
        return redirect('/login')
