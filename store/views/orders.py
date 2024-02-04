from django.views import View
from django.shortcuts import render,redirect
from store.models.product  import Product
from store.models.orders import Order
from store.models.customer import Customer
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class OrderView(View):
    @method_decorator(auth_middleware)            # to use decorator with methods you need different way like here.
    def get(self,request):
        customer_id=request.session.get('customer')
        orders=Order.get_orders_by_customer_id(customer_id)
        # print(orders)
        return render(request,'orders.html',{'orders':orders})

        
