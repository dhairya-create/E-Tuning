from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.views import View

# Create your views here.
class About(View):
    def get(self, request):
        return render(request,'about.html')