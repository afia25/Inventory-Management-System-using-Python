from django.db import models



class Products(models.Model):
    product_name=models.CharField(max_length=30,default='')
    category_name=models.CharField(max_length=30,default='')
    description=models.CharField(max_length=100,default='')
    buying_price=models.IntegerField(default=1)
    selling_price=models.IntegerField(default=1)
    purchase=models.IntegerField(default=1)
    sale=models.IntegerField(default=1)
    stock =models.IntegerField(default=1)

    def __str__(self):
        return self.product_name


    #supplier=models.ForeignKey(SupplierInfo, on_delete=models.SET_NULL)


class CustomerInfo(models.Model):
    user_id=models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    delivary_address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=150)
    delivery_within_what_time=models.CharField(max_length=150)
    alternative_contact_name = models.CharField(max_length=150)
    alternative_contact_number = models.CharField(max_length=150)
    payment_method=models.CharField(max_length=150)
    profile_picture=models.ImageField(default='default.jpg',upload_to='profile_pictures')
    product= models.ForeignKey(Products,null=True,on_delete=models.SET_NULL,blank=True)

    quantity=models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class User_Details(models.Model):
    name = models.CharField(max_length=30)
    customer_id = models.CharField(max_length=30,default='')
    delivary_address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=150)
    delivery_within_what_time=models.CharField(max_length=150)
    alternative_contact_name = models.CharField(max_length=150)
    alternative_contact_number = models.CharField(max_length=150)
    payment_method=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    discount = models.IntegerField()
    delivery_charge = models.IntegerField()
    customer_id=models.CharField(max_length=10,default='')
    total_price = models.IntegerField()
    payment = models.IntegerField()
    due = models.IntegerField()
    total = models.IntegerField(default=0)

    prod_id=models.CharField(max_length=10,default='')
    name_of_product = models.CharField(max_length=50, default='')
    quantity=models.IntegerField(default=0)
    name_of_customer=models.CharField(max_length=50,default='')









class Sales(models.Model):
    invoice = models.ForeignKey(Invoice,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Products,null=True, on_delete=models.SET_NULL)
    pofit = models.IntegerField()
    customer = models.ForeignKey(CustomerInfo,null=True, on_delete=models.SET_NULL)




class SupplierInfo(models.Model):
    supplier_name = models.CharField(max_length=50,default='')
    supplier_email = models.CharField(max_length=50,default='')
    supplier_contact = models.CharField(max_length=11,default='')
    productId=models.CharField(max_length=11,default='')



class Order(models.Model):
    product_id=models.CharField(max_length=10)
    user_id =models.CharField(max_length=10)
    quantity=models.IntegerField(default=0)





class Users(models.Model):
    password=models.CharField(max_length=30)
    username=models.TextField()
    first_name=models.TextField()
    last_name=models.TextField()
    email=models.EmailField()
