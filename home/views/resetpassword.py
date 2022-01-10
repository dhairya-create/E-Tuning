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

class Resetpassword(View):
    def get(self,request):
        return render(request,"changepass.html")
    
    def post(self,request):
        new_pass = request.POST.get('new')
        retype_pass = request.POST.get('retype')
        error_messages = None

        if new_pass != retype_pass:
            error_messages = "Passwords do not match !"
        elif len(new_pass) < 8:
            error_messages = "Password needs minimum 8 characters"

        if not error_messages:
            username = request.session['username']
            user = Register.objects.get(username = username)
            user.password = make_password(new_pass)
            user.save()
            return redirect('/login')
        else:
            return render(request,"changepass.html",{'error' : error_messages}) 