from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.hashers import make_password,check_password
from store.models.product import Product 
from store.models.category import Category
from store.models.customer import Customer
from django.views import View 


class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
            postData=request.POST
            first_name=postData.get('firstname')
            last_name=postData.get('lastname')
            phone=postData.get('phone')
            email=postData.get('email')
            password=postData.get('password')
            customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)

            value={
                'first_name':first_name,
                'last_name':last_name,
                'phone':phone,
                'email':email
            }
            error_msg=self.validateCustomer(customer)
            
            if not error_msg:
                customer.password=make_password(customer.password)
                customer.register()
                return redirect('homepage')
            else:
                data={
                    'error':error_msg,
                    'values':value
                }
                return render(request,'signup.html',data)
            
    def validateCustomer(self,customer):
            error_msg=None
        
            if not customer.first_name:
                error_msg='First Name Required!!'
            elif len(customer.first_name)<4:
                error_msg='First Name must be atleast 4 characters long'
            elif not customer.last_name:
                error_msg='Last Name Required!!'
            elif len(customer.last_name)<4:
                error_msg='Last Name must be atleast 4 characters long'
            elif not customer.phone:
                error_msg='Phone Number Required!!'
            elif len(customer.phone)!=10:
                error_msg='Phone Number have 10 digits'
            elif not customer.password:
                error_msg='Password Required!!'
            elif len(customer.password)<6:
                error_msg='Password must have atleast 6 characters'
            elif len(customer.email)<5:
                error_msg='email must have atleast 5 characters '

            isExist=customer.isExist()
            if isExist:
                error_msg="Email Address already Registered!!"
            return error_msg