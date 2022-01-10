from django.views import View
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from home.models import Cart,Order,Register,Product
from django.contrib import messages
from django.contrib.auth.hashers import check_password

class Login(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = Register.get_customer_by_username(username)
        cart= {}
        message = {}
        request.session['cart'] = cart
        request.session['message'] = message
        error_message= None
        if customer:
            flag  = check_password(password , customer.password)
            if flag:
                request.session['customer'] = customer.id
                cart_items = Cart.get_cart_by_customer_id(customer.id)
                for i in cart_items:
                    cart[str(i.product.id)] = i.quantity
                    message[str(i.product.id)] = i.message
                    request.session['cart'] = cart
                    request.session['message'] = message
                messages.success(request, " You're Logged In !")
                return redirect('/index') 
            else:
                error_message="Email or Password invalid"
        else:
            error_message="Email or Password invalid"

        return render(request,'login.html',{'error':error_message})
