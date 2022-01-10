from django.db import models
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122) 
    email = models.CharField(max_length=122)
    subject = models.TextField()
    des = models.TextField()
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.email
    
class Category(models.Model):
    name = models.CharField(max_length=122)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
    
class Product(models.Model):

    category= models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    product_name = models.CharField(max_length=122)
    product_des = models.CharField(max_length=200,default='',null=True,blank=True)
    product_price = models.IntegerField(default=0)
    product_quantity = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to="product")

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category= category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def search_product(query):
        return Product.objects.filter(product_name__icontains=query)
        
    @staticmethod
    def  get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    def __str__(self):
        return self.product_name  

class Register(models.Model):
    
    fname = models.CharField(verbose_name=("First Name"),max_length=122)
    lname = models.CharField(verbose_name=("Last Name"),max_length=122)
    email = models.CharField(verbose_name=("Email"),max_length=122)
    phone = models.CharField(verbose_name=("Phone"),max_length=100)
    add = models.CharField(verbose_name=("Address"),max_length=150)
    username = models.CharField(verbose_name=("User Name"),max_length= 150,default="none")
    pin = models.CharField(verbose_name=("Pincode"),max_length=15)
    password = models.CharField(verbose_name=("Password"),max_length=122)
    usertype = models.CharField(verbose_name=("User Type"),max_length=150,default="customer")

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Register.objects.get(username = username)
        except:
            return False

    def __str__(self):
        return self.username

class Artist2(models.Model):
    artist_id = models.ForeignKey(Register,on_delete=models.CASCADE)
    category = models.CharField(verbose_name=("Category"),max_length=50, default="empty")
    des = models.TextField()
    image = models.ImageField(upload_to="artist")

    def __str__(self):
        return self.artist_id.username

    @staticmethod
    def search_artist(query):
        return Artist2.objects.filter(artist_id__fname__icontains=query)
    
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Register,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=120,default="",blank=True)
    phone = models.CharField(max_length=120,default="",blank=True)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer_id(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')

class Cart(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Register,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    message = models.BooleanField(default = True, null = True)
    
    @staticmethod
    def get_cart_by_customer_id(customer_id):
        return Cart.objects.filter(customer= customer_id)

class Sell(models.Model):
     
    fname = models.CharField(verbose_name=("First Name"),max_length=122)
    lname = models.CharField(verbose_name=("Last Name"),max_length=122)
    email = models.CharField(verbose_name=("Email"),max_length=122)
    phone = models.CharField(verbose_name=("Phone"),max_length=100)
    add = models.CharField(verbose_name=("Address"),max_length=150)
    product_image = models.ImageField(upload_to="product")
    product_name = models.CharField(max_length=122)
    product_des = models.CharField(max_length=200,default='',null=True,blank=True)
    product_price = models.IntegerField(default=0, null = False)
    category = models.CharField(max_length=122)
    status = models.BooleanField(default=False)



    
       