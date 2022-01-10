from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.views import View

class Index(View):
    def get(self, request):
        print("you are : " , request.session.get('customer_username'))
        return render(request,'index.html')
    
