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

class Profile(View):
    def get(self,request):
        id = request.session['customer']
        user = Register.objects.get(id = id)
        if user.usertype == "artist":
           art = Artist2.objects.get(artist_id__id__icontains = id)
        else:
            art = None
        data = {
            'user' : user,
            'art' : art,
        }
        return render(request,'demo.html', data)