from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.customer import Customer
from django.views import View 
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class Profile(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        return render(request,'profile.html')


    

