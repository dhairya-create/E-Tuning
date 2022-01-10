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


class Signup(View):
    def get(self,request):
        return render(request,'register.html')
    
    def post(self,request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user = request.POST.get('tab')
        add = request.POST.get('add')
        username = request.POST.get('username')
        des = request.POST.get('des')
            
        category = request.POST.get('category')
        pin = request.POST.get('pin')
        password = request.POST.get('password')
        retypepass = request.POST.get('retypepass')
        #validations
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        Pattern = re.compile("(0/91)?[6-9][0-9]{9}")
        value={
            'fname': fname,
            'lname': lname,
            'email': email,
            'phone': phone,
            'des': des,
            'username': username,
            'add': add,
            'pin': pin,
        }
        error_message = None   
        customer = Register(fname=fname,
                            lname=lname,
                            phone=phone,
                            email=email,
                            add=add,
                            pin=pin,
                            password=password,
                            username= username,
                            usertype= user) 

        if(not Pattern.match(phone)):
            error_message="invalid phone number"
        elif(not re.search(regex, email)):
            error_message="invalid email id"
        elif(password != retypepass):
            error_message="passwords do not match"
        elif len(password) < 8:
            error_message="password length should be 8 or more"
        elif(Register.objects.filter(username = username)):
            error_message="username already exists"
        elif(user == "artist"):
            image = request.FILES['image']
            if(not image):
                error_message="Please Attach A Picture"
            elif(not des):
                error_message="Enter Description"
            elif(not category):
                error_message="Category Required"

        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            if(user == "artist"):
                image = request.FILES['image']
                artist = Artist2(artist_id= customer,des=des, image= image, category= category)
                artist.save()
            
            messages.success(request, " Registration Sucessful ")
            return redirect('/index')
        else:
            data ={
                'value': value,
                'error': error_message,
            }
            return render(request,'register.html',data)