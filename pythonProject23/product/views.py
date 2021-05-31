

from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Products
from django.contrib import messages
from .models import *

from .form import *







#View Cart
def productList(request):
    if (request.method=='POST'):
        return redirect('userorder')

    buyForm=BuyForm()
    return render(request,'product/productList.html',{'form':buyForm})





def clothes(request):
    a = Products.objects.get(id__exact='1')
    b = Products.objects.get(id__exact='2')
    c = Products.objects.get(id__exact='3')

    if (request.method=='POST'):
        clothesform=ClothesForm(request.POST)
        if (clothesform.is_valid()):
            clothesform.save()
            return redirect('clothes')
        else:
            return render(request, 'product/clothes.html', {'clothesform': clothesform,'a': a,'b': b,'c': c})
    else:
        a = Products.objects.get(id__exact='1')
        b = Products.objects.get(id__exact='2')
        c = Products.objects.get(id__exact='3')
        clothesform = ClothesForm()
        return render(request, 'product/clothes.html', {'clothesform': clothesform,'a': a,'b': b,'c': c})


def electronics(request):
    a = Products.objects.get(id__exact='4')
    b = Products.objects.get(id__exact='5')
    c = Products.objects.get(id__exact='6')

    if (request.method=='POST'):
        electronicsform=ElectronicsForm(request.POST)
        if (electronicsform.is_valid()):
            electronicsform.save()
            return redirect('electronics')
        else:
            return render(request, 'product/electronics.html', {'electronicsform': electronicsform,'a': a,'b': b,'c': c})
    else:
        a = Products.objects.get(id__exact='4')
        b = Products.objects.get(id__exact='5')
        c = Products.objects.get(id__exact='6')
        electronicsform = ElectronicsForm()
        return render(request, 'product/electronics.html', {'electronicsform': electronicsform,'a': a,'b': b,'c': c})






    #buyForm=BuyForm()
    #return render(request,'product/clothes.html',{'form':buyForm})

def food(request):
    a = Products.objects.get(id__exact='7')
    b = Products.objects.get(id__exact='8')
    c = Products.objects.get(id__exact='9')
    if (request.method=='POST'):
        foodform=FoodForm(request.POST)
        if (foodform.is_valid()):
            foodform.save()
            return render(request, 'product/productList.html')
            #return redirect('food')
        else:
            return render(request, 'product/food.html', {'foodform': foodform,'a': a,'b': b,'c': c})
    else:
        a = Products.objects.get(id__exact='7')
        b = Products.objects.get(id__exact='8')
        c = Products.objects.get(id__exact='9')
        foodform = FoodForm()
        return render(request, 'product/food.html', {'foodform': foodform,'a': a,'b': b,'c': c})













def order(request):
    if (request.method=='POST'):
        orderform = OrderForm()
        #orders = Order.objects.all().delete()
        firstobj=Order.objects.first()
        firstobj.delete()
        orders = Order.objects.all()
        return render(request, 'product/order.html', {'orders': orders, 'orderform': orderform})
        #return redirect('order')

    orderform = OrderForm()
    orders = Order.objects.all()
    return render(request,'product/order.html',{'orders': orders, 'orderform': orderform})

#Buy Now
def userorder(request):
    if (request.method=='POST'):
        return redirect('user_Details')

    userorderform = UserOrderForm()
    orders = Order.objects.all()
    return render(request, 'product/userorder.html', {'orders': orders, 'userorderform': userorderform})


    #return render(request,'product/productList.html',{'form':buyForm})




def stockReport(request):
    stocks = Products.objects.all()
    return render(request,'product/stockReport.html',{'stocks':stocks})


def makeinvoice(request):
    if (request.method=='POST'):
        dform = DeleteInvoiceForm()
        #invoices=Invoice.objects.all().delete()
        firstobj = Invoice.objects.first()
        firstobj.delete()
        invoices=Invoice.objects.all()
        #return redirect('empHome')
        return render(request, 'product/makeinvoice.html', {'invoices': invoices, 'dform': dform})


    dform = DeleteInvoiceForm()
    invoices=Invoice.objects.all()
    return render(request,'product/makeinvoice.html',{'invoices': invoices, 'dform': dform})

    #invoices=Invoice.objects.all()
    #return render(request, 'product/makeinvoice.html', {'invoices':invoices})


def due(request):
    if (request.method=='POST'):
        dict=request.POST
        a=dict['id']
        b=User_Details.objects.get(customer_id__exact=a)
        invoices = Invoice.objects.filter(due__gt=0)
        return render(request, 'product/due.html', {'invoices': invoices,'b':b})


    b=' '
    invoices=Invoice.objects.filter(due__gt=0)
    return render(request, 'product/due.html', {'invoices':invoices,'b':b})

def outOfStock(request):
    if (request.method=='POST'):
        dict=request.POST
        a=dict['pid']
        b=SupplierInfo.objects.get(productId__exact=a)
        products = Products.objects.filter(stock=0)
        return render(request, 'product/outOfStock.html', {'products': products,'b':b})


    b=' '
    products=Products.objects.filter(stock=0)
    return render(request, 'product/outOfStock.html', {'products':products,'b':b})



def addproduct(request):
    if (request.method=="POST"):
        addproductform = AddProductForm(request.POST)
        if (addproductform.is_valid()):
            addproductform.save()

           # views1.stock(request)
            return redirect('adminHome')
        else:
            context = {
                'addproductform': addproductform,
            }
            return render(request, 'product/addproduct.html', context)
    else:
        addproductform = AddProductForm()
        context = {
            'addproductform': addproductform,
        }
        return render(request, 'product/addproduct.html', context)


def invoice(request):
    if (request.method=="POST"):
        invoiceform = InvoiceForm(request.POST)
        if (invoiceform.is_valid()):
            invoiceform.save()
            return redirect('invoice')
        else:
            context = {
                'invoiceform': invoiceform,
            }
            return render(request, 'product/invoice.html', context)
    else:
        invoiceform = InvoiceForm()
        context = {
            'invoiceform': invoiceform,
        }
        return render(request, 'product/invoice.html', context)


def user_Details(request):
    if (request.method=='POST'):
        userdetailsform = UserDetailsForm(request.POST)
        if (userdetailsform.is_valid()):
            userdetailsform.save()
            return redirect('profile')

        else:
            context = {
                'userdetailsform': UserDetailsForm
            }
            return render(request, 'product/user_Details.html', context)

    else:
        userdetailsform = UserDetailsForm()
        context = {
            'userdetailsform': UserDetailsForm
        }
        return render(request, 'product/user_Details.html', context)


def salesReport(request):
    if (request.method=='POST'):
        dict=request.POST
        a=dict['pid']
        b=Products.objects.get(id__exact=a)
        sale=int(b.sale)
        stock=int(b.stock)
        q = dict['quan']
        quantity=int(q)
        inc_sale=sale+quantity
        dec_stock = stock - quantity

        b.sale=inc_sale
        b.stock=dec_stock
        b.save()
        stocks = Products.objects.all()
        return render(request, 'product/salesReport.html', {'stocks': stocks})


    stocks = Products.objects.all()
    return render(request, 'product/salesReport.html', {'stocks': stocks})


def cancelorder(request):
    if (request.method=='POST'):
        dict=request.POST
        a=dict['id']
        b=Order.objects.get(product_id__exact=a)
        b.delete()
        orders = Order.objects.all()
        return render(request, 'product/cancelorder.html', {'orders': orders})


    orders = Order.objects.all()
    return render(request, 'product/cancelorder.html', {'orders': orders})






