from django.db import models
from .product import Product
from .customer import Customer
import datetime
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)  # here customer is object not customer id
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=50,default='')
    phone=models.CharField(max_length=10,default='')
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)


    def placeOrder(self):
        self.save()  #data will be saved here

    @staticmethod 
    def get_orders_by_customer_id(customer_id):
        return Order.\
            objects.\
                filter(customer=customer_id)\
                .order_by('-date')
    
    def __str__(self):
        return str(self.customer.id)