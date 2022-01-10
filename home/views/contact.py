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

class Contact(View):
    def get(self,request):
        return render(request,'contact.html')

    def post(self,request):
        error_message = None
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        des = request.POST.get('des')
        value={
            'name': name,
            'email': email,
            'subject': subject,
            'des': des,
        }
        if(not re.search(regex, email)):
            error_message="invalid email id"
        
        if not error_message:
            contact = Contact(name=name, email=email, subject=subject, des=des)
            contact.save()
            messages.success(request, 'Your message has been sent')
            return redirect('/index')
        else:
            data = {
                'values' : values,
                'error' : error_message,
            }
            return render(request,'contact.html',data)