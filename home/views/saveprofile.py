from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from home.models import Register,Artist2
from django.contrib import messages
from django.views import View

# Create your views here.

class Saveprofile(View):
    def post(self,request):
        fname = request.POST.get('fname')
        print(fname)
        lname = request.POST.get('lname')
        print(lname)
        email = request.POST.get('email')
        usertype = request.POST.get('usertype')
        username = request.POST.get('username')
        add = request.POST.get('add')
        pin = request.POST.get('pin')
        id = request.session['customer']
       
        customer = Register.objects.get(id = id)
        customer.fname = fname
        customer.lname = lname
        customer.email = email
        customer.pin = pin
        customer.add = add
        customer.save() 
        if usertype == "artist":
            des = request.POST.get('des')
            cat = request.POST.get('cat')
            artist = Artist2.objects.get(artist_id__id__icontains = id)
            artist.des = des
            artist.category = cat
            artist.save()
        return redirect('/profile')