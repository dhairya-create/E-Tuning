from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from home.models import Sell,Cart,Order,Contact,Register,Product,Artist2,Category
from django.contrib import messages
import re
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class Artist(View):
    def get(self,request):
        cat = Artist2.objects.all().values_list('category', flat = True).distinct()
        print(cat)
        var = request.GET.get('list')
        if var:
            art = Artist2.objects.filter(category = var)
        else:
            art = Artist2.objects.all()
        data = {
            'cat' : cat,
            'art' : art,
        }
        return render(request,'artist.html',data)

    def post(self,request):
        cat = Artist2.objects.all().values_list('category', flat = True).distinct()
        query = request.POST.get('search_artist')
        if query:
            art = Artist2.search_artist(query)
            if not art:
                messages.error(request,' No Such Artist Available')
                art = Artist2.objects.all()
        else:
            art = Artist2.objects.all()
        data = {
            'cat' : cat,
            'art' : art,
        }
        return render(request, 'artist.html',data)