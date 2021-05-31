from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm , forms
from .models import *

class BuyForm(forms.Form):
    pass

class UserOrderForm(forms.Form):
    pass

class OrderForm(forms.Form):
    pass


class DeleteInvoiceForm(forms.Form):
    pass

class AddProductForm(forms.ModelForm):

    category_name = forms.CharField(max_length=30, required=False)
    description = forms.CharField(max_length=100, required=False)
    buying_price= forms.IntegerField( required=False)
    selling_price = forms.IntegerField( required=False)
    purchase = forms.IntegerField( required=False)
    sale= forms.IntegerField( required=False)
    class Meta:
        model=Products
        fields=[
            'product_name',

            'category_name',
            'description',
            'buying_price',
            'selling_price',
            'purchase',
            'sale',
            'stock',

        ]

class InvoiceForm(forms.ModelForm):

    class Meta:
        model=Invoice
        fields=[
            'name_of_customer',
            'customer_id',

            'name_of_product',
            'prod_id',
            'quantity',
            'total_price',
            'delivery_charge',
            'discount',
            'total',
            'payment',
            'due',


        ]

class ClothesForm(forms.ModelForm):

    class Meta:
        model=Order
        fields=[
            'product_id',
            'user_id',
            'quantity',
        ]



class ElectronicsForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'product_id',
            'user_id',
            'quantity',
        ]


class FoodForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'product_id',
            'user_id',
            'quantity',
        ]


class UserDetailsForm(forms.ModelForm):
    alternative_contact_name= forms.CharField(max_length=150,required=False)
    alternative_contact_number=forms.CharField(max_length=150,required=False)
    delivery_within_what_time=forms.CharField(max_length=150,required=False)
    class Meta:
        model = User_Details
        fields = [
            'name',
            'customer_id',
            'delivary_address',
            'city',
            'area',
            'contact_number',
            'delivery_within_what_time',
            'alternative_contact_name',
            'alternative_contact_number',
            'payment_method',
        ]


class StockForm(forms.Form):
    product_id=forms.CharField(label='Product Id',max_length=30)
    quantity=forms.IntegerField(label='Quantity')
