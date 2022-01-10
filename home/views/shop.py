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

class Shop(View):
    def get(self, request):
        product = None
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if category_id:
            cat = Category.objects.get(id = category_id)
            if cat.name == 'Refurbished':
                product = Sell.objects.filter(status = True)
            else:
                product = Product.get_all_products_by_categoryid(category_id)
        else:
            product = Product.get_all_products()
        data = {
            'product' : product,
            'categories': categories,
        }
        return render(request,'shop.html',data)
        
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        print(cart)
        message = request.session.get('message')
        remove = request.POST.get('remove')
        request.session.get('customer')
        stock = Product.objects.get(id = product)
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                        message.pop(product)
                        #message[product] = False
                    else:
                        cart[product] = quantity - 1
                        message[product] = False
                else:
                    if int(stock.product_quantity) > quantity: 
                        cart[product] = quantity + 1
                    else:
                        print("out of stock no cart items")
                        message[product] = True
            else:
                if int(stock.product_quantity) > 0:
                    cart[product] = 1
                else:
                    print("out of stock no cart items")
                    message[product] = True
        else:
            cart = {}
            message = {}
            if int(stock.product_quantity) > 0:
                cart[product] = 1
                message[product] = False
            else:
                print("out of stock no cart items")
                message[product] = True
        request.session['cart'] = cart
        request.session['message'] = message
        return redirect('/shop')
