from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.customer import Customer
from django.views import View 
from store.models.product import Product

class Cart(View):
    def get(self,request):
        a=request.session.get('cart')
        l=[]
        if a:
            l=list(a.keys())
        else:
            return redirect('homepage')

        products=Product.get_products_by_id(l)
        return render(request,'cart.html',{'products':products})
    
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
         
        customer=Customer.get_customer_by_email(email)
        error_msg=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer']=customer.id  # as customer_id is unique we don't need email id
                # request.session['email']=customer.email 
                return redirect('homepage')
            else:
                error_msg='Incorrect Password!!'
        else:
            error_msg='User not registered!!'
        return render(request,'login.html',{'error':error_msg})
    

  
def logout(request):
    request.session.clear()
    return redirect('login')


