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

class Search(View):
    def post(self,request):
        product = None
        query = request.POST.get('search_item')
        categories = Category.get_all_categories()
        if query:
            product = Product.search_product(query)
            if not product:
                messages.error(request, ' No Such Product Found !')
                product = Product.get_all_products()
        else:
            product = Product.get_all_products()
        data = {
            'product' : product,
            'categories': categories, 
        }
        return render(request, 'shop.html',data)
