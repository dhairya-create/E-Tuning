from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from home.models import Sell,Cart,Order,Contact,Register,Product,Artist2,Category
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class Changepassword(View):
    def post(self,request):
        current_pass = request.POST.get('current')
        new_pass = request.POST.get('new')
        id = request.session['customer']
        user = Register.objects.get(id = id)
        error_messages = None
        if not check_password(current_pass,user.password):
            error_messages = "current password does not match!"
            return render(request,"reset.html",{'error':error_messages})
        else:
            user.password = make_password(new_pass)
            user.save()
            messages.success(request,"Your Password has been changed !")
            return render(request,'demo.html')
    #return render(request,'reset.html')        
     