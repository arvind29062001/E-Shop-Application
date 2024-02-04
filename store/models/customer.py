from django.db import models 
class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)

    def register(self):
        self.save()

    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        else :
            return False
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False 
       



    
