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

class Passforget(View):
    def post(self,request):
        username = request.POST.get('username')
        print("received from form ",username)
        try:
            print("textbox",username)
            user = Register.objects.get(username = username)
            request.session['username'] = username
            print(request.session['username'])
            print('*test')
            from_email = 'snjain990@gmail.com' 
            sub = 'RESET PASSWORD.'   # write a subject to send otyher user
            # msg = 'hello python<br>' #body msg
            # link_send = 'http://localhost:8000/index'
            # msg += link_send
            msg = "Click on this link to reset your password! "
            msg += """http://localhost:8000/resetpassword"""
            user_email_list = [user.email]
            #user_email_list = ['snjain990@gmail.com']
            send_mail(sub, msg, from_email, user_email_list)
            # subject = 'your subject'
            # message = 'write your message here'
            # recepient = 'mishelshah07@gmail.com'
            # send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
            #return HttpResponse("mail has been sent")
            return render(request,"mailsent.html")
        except:
            print('Email 315 error')
            print("no user")
            messages.error(request,"No such user found")
            return render(request,"username.html")    