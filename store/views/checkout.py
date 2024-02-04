from django.views import View
from django.shortcuts import render,redirect
from store.models.product  import Product
from store.models.orders import Order
from store.models.customer import Customer
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
class CheckOut(View):
    @method_decorator(auth_middleware)
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        for product in products:
            order=Order(customer=Customer(id=customer),product=product,price=product.price,address=address,phone=phone,quantity=cart.get(str(product.id)))
            order.placeOrder()
        request.session['cart']={}
        return redirect('cart')