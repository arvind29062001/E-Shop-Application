from django.contrib import admin
from django.urls import path
from store.views import home,login,signup
from store.views import cart
from store.views import checkout
from store.views import orders
from store.views import profile

urlpatterns = [
    path('', home.Index.as_view(),name='homepage'),
    path('signup',signup.Signup.as_view(), name='signup'),
    path('login',login.Login.as_view(),name='login'),
    path('logout',login.logout,name='logout'),
    path('cart',cart.Cart.as_view(),name='cart'),
    path('check-out',checkout.CheckOut.as_view(),name='checkout'),
    path('orders',orders.OrderView.as_view(),name='orders'),
    path('profile',profile.Profile.as_view(),name='profile'),
    
]