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


class Sellpage(View):
    def get(self,request):
        return render(request,"sell.html")
    
    def post(self,request):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        Pattern = re.compile("(0/91)?[6-9][0-9]{9}")
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        category = request.POST.get('type')
        phone = request.POST.get('phone')
        address = request.POST.get('add')
        des = request.POST.get('des')
        price = request.POST.get('price')
        image = request.FILES['image']
        product_name = request.POST.get('product_name')
        error_message = None
        
        if(not Pattern.match(phone)):
            error_message="invalid phone number"
        elif(not re.search(regex, email)):
            error_message="invalid email id"
        values={
            'fname' : fname,
                'lname' : lname,
                'email' : email,
                'category' : category,
                'name' :  product_name,
                'phone' : phone,
                'des' : des,
                'add' : address,
                'price' : price
        }
        if not error_message:
            obj = Sell(fname=fname,
                lname=lname,
                email=email,
                category=category,
                product_name= product_name,
                phone = phone,
                product_des = des,
                add = address,
                product_image = image,
                product_price = price)
            obj.save()
            return redirect('/index')
        else:
            data ={
                'values': values,
                'error' : error_message,
            }
            return render(request,"sell.html",data)