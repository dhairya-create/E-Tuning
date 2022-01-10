from django.contrib import admin
from home.models import Sell,Cart,Order,Contact,Register,Category,Product,Artist2
from django.contrib.auth.models import Group,User

admin.site.site_header = 'E-tuning Admin'

class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'category', 'product_quantity', 'product_image']
    list_filter = ['category']

class AdminRegister(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'username', 'usertype', 'email', 'phone']
    list_filter = ['username','usertype']

class AdminOrder(admin.ModelAdmin):
    list_display = ['customer', 'product', 'price', 'quantity']
    list_filter = ['date','customer']

class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date']
    list_filter = ['name']    

class AdminSell(admin.ModelAdmin):
    list_display = ['fname', 'email', 'product_name', 'product_image', 'product_price', 'status']
    list_filter = ['status']
   
class AdminCart(admin.ModelAdmin):
    list_display = ['customer', 'product', 'quantity']
    list_filter = ['customer']

class AdminArtist2(admin.ModelAdmin):
    list_display = ['artist_id', 'des', 'category','image']
    list_filter = ['artist_id']

# Register your models here.
admin.site.register(Contact,AdminContact)
admin.site.register(Register, AdminRegister)
admin.site.register(Category)
admin.site.register(Sell,AdminSell)
admin.site.register(Product, AdminProduct)
admin.site.register(Artist2,AdminArtist2)
admin.site.register(Order, AdminOrder)
admin.site.register(Cart,AdminCart)
admin.site.unregister(Group)
admin.site.unregister(User)