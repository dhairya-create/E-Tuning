from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from datetime import datetime
from home.models import Sell,Cart,Order,Contact,Register,Product,Artist2,Category
from django.contrib import messages
from django.views import View

class Checkout(View):
    def get(self,request):
        try:
            flag = request.session['order']
            print(flag)
            if flag:
                #customer = request.session.get('customer')
                #orders = Order.get_orders_by_customer_id(customer)
                #print(orders)
                request.session['order'] = False
                return redirect('/orders')
                #return render(request, 'orders.html',{'orders' : orders})
                #return render(request,"orders.html")
            else:
                ids = list(request.session['cart'].keys())
                products = Product.get_products_by_id(ids)
                id = request.session['customer']
                customer = Register.objects.get(id = id)
                data = {
                    'products' : products,
                    'customer' : customer,
                }
                return render(request, "checkout.html",data)
        except:
            request.session['order'] = False
            ids = list(request.session['cart'].keys())
            products = Product.get_products_by_id(ids)
            id = request.session['customer']
            customer = Register.objects.get(id = id)
            data = {
                'products' : products,
                'customer' : customer,
            }
            return render(request, "checkout.html",data)
    
    def post(self,request):
        print("orders recieved")
        choice = request.POST.get('check')
        customer = request.session.get('customer')
        print(customer)
        user = Register.objects.get(id = customer)
        if choice:
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pin = request.POST.get('pin')
            address += " " + city + "  " + state + " " + pin
        else:
            address = user.add
            phone = user.phone
            pin = user.pin
        cart = request.session.get('cart')
        product_id = Product.get_products_by_id(list(cart.keys()))
        for product in product_id:
            order = Order(customer= Register(id = customer),
                        product=product,
                        price=product.product_price,
                        address= address,
                        phone= phone,
                        quantity = cart.get(str(product.id)))  
            qty = Product.objects.get(id = product.id)
            qty.product_quantity = qty.product_quantity - cart.get(str(product.id))
            qty.save()
            order.placeOrder()
        request.session['cart'] = {}
        request.session['order'] = True
        return HttpResponseRedirect("http://www.instamojo.com/@ankurpatel")