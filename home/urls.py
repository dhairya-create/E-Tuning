from django.contrib import admin
from django.urls import path
from home import views
from .views import about,artist,cart,changepassword,checkout,contact,index,logout,orders,passforget,profile,register,resetpassword,saveprofile,search,sellpage,shop,username,login
#from .middleware.auth import auth_middleware

urlpatterns = [
    path("",index.Index.as_view(),name='home'),
    path("index",index.Index.as_view(),name='home'),
    path("about", about.About.as_view(),name='about'),
    path("shop", shop.Shop.as_view(),name='shop'),
    path("sellpage", sellpage.Sellpage.as_view(),name='sellpage'),
    path("artist",artist.Artist.as_view(),name='artist'),
    path("cart",cart.Cart.as_view(),name='cart'),
    path("checkout",checkout.Checkout.as_view(),name='checkout'),
    path("contact",contact.Contact.as_view(),name='contact'),
    #path("submitcontact",contact.Contact.as_view(),name='contact'),
    path("login",login.Login.as_view(),name='login'),
    path("logout",logout.Logout.as_view(),name="logout"),
    path("register",register.Signup.as_view(),name='register'),
    #path("submitregister",views.register,name='register'),
    path("orders",orders.Orders.as_view(),name='orders'),
    path("search",search.Search.as_view(),name='search'),
    path("profile",profile.Profile.as_view(),name='profile'),
    path("changepassword",changepassword.Changepassword.as_view(),name='changepassword'),
    path("passforget",passforget.Passforget.as_view(),name='passforget'),
    path("resetpassword",resetpassword.Resetpassword.as_view(),name='resetpassword'),
    path("username",username.Username.as_view(),name="username"),
    path("saveprofile",saveprofile.Saveprofile.as_view(),name="saveprofile"),
]
