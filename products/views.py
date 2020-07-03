from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Cart, Vegetable, Dal_Rice
from .models import Cookies_Snakes, Order
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import date


def products(request):
    cart = Cart.objects.all()
    value=0
    print(f"\n\n\n\n\n\t\t\t\t{request.user.username}\n\n\n\n")
    for i in cart:
        if request.user.username == i.name:
            value = value + 1
    product = Product.objects.all()
    return render(request, 'index.html', {'products': product, 'value': value})


def vegetable(request):
    cart = Cart.objects.all()
    value = 0
    for i in cart:
        if request.user.username == i.name:
            value = value + 1
    product = Product.objects.all()
    veg = Vegetable.objects.all()
    return render(request, 'vegetable.html', {'vegetable':veg, 'value': value})


def dal_rice(request):
    cart = Cart.objects.all()
    value = 0
    for i in cart:
        if request.user.username == i.name:
            value = value + 1
    product = Dal_Rice.objects.all()
    return render(request, 'dal_rice.html', {'dal_rice': product, 'value': value})


def cookie_snack(request):
    cart = Cart.objects.all()
    value = 0
    for i in cart:
        if request.user.username == i.name:
            value = value + 1
    product = Cookies_Snakes.objects.all()
    return render(request, 'cookies_snack.html', {'dal_rice': product, 'value': value})


def cart(request):
    if request.method == 'POST':
        c = Cart()
        item_name = request.POST["item_name"]
        item_price = request.POST["item_price"]
        item_url = request.POST["item_url"]
        name = request.POST["name"]
        quantity = request.POST["quantity"]
        product = request.POST["product"]
        c.item = item_name
        c.name = name
        c.product = product
        c.item_price = item_price
        c.item_url = item_url
        c.quantity = quantity
        c.save()
        value = 0
        add=0
        cart = Cart.objects.all()
        for i in cart:
            if name == i.name:
                value = value + 1
            if name == i.name:
                add = add + int(i.item_price)
        # messages.info(request, f"{value}")
        messages.info(request, f"Item {item_name} has been added to your cart 😊")
        return render(request, "cart.html",{'value':value, 'add':add, 'cart': cart})
    else:
        cart = Cart.objects.all()
        name = str(request.user)
        add=0
        value=0
        for i in cart:
            if name == i.name:
                add = add + int(i.item_price)
            if name == i.name:
                value = value + 1
        return render(request, "cart.html", {'cart': cart, 'add':add, 'value':value})


def remove(request):
    a = request.POST["info"]
    Cart.objects.filter(id=a).delete()
    messages.info(request, "Item has been removed from your Cart")
    return redirect('cart')


def clear_cart(request):
    print("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\tThis is cart\n\n\n\n\n\n")
    username = request.POST['username']
    Cart.objects.filter(name=username).delete()
    messages.info(request, 'Your cart is empty!!')
    return redirect('cart')


def main(request):
    return render(request, 'main.html')


def checkout(request):
    user = User.objects.all()
    return render(request,'checkout.html', {'user':user})


def buy(request):
    if request.method == "POST":
        user = request.POST['user']
        fullname = request.POST['fullname']
        phone = request.POST['phone']
        email = request.POST["email"]
        city = request.POST["city"]
        district = request.POST["district"]
        address = request.POST["address"]
        note = request.POST["note"]
        try:
            phone=int(phone)
            if len(str(phone)) != 10:
                messages.info(request, f"Phone number invalid\n")
                return render(request, "checkout.html")
        except:
            messages.info(request, "please enter correct phone number\n")

        cart = Cart.objects.all()
        c = Order()
        item = ''
        for i in cart:
            if i.name == str(request.user):
                item = i.item + ',' + item
        c.user=request.user.username
        c.fullname=fullname
        c.email=email
        c.phone=phone
        c.city=city
        c.district=district
        c.address=address
        c.note=note
        c.item=item
        c.date=str(date.today())
        if email=='' and city=='':
            messages.info(request, "Please fill all the details before going to check out\n")
            return render(request, "checkout.html")
        elif address=='':
            messages.info(request, "Please fill your address\n")
            return render(request, "checkout.html")
        else:
            cart = Cart.objects.all()
            money = 0
            for i in cart:
                if str(request.user) == i.name:
                    money = money + int(i.item_price)
            if money == 0:
                messages.info(request, "Please add items in your cart before check out\n")
            c.bill_amount = money


            import smtplib
            from email.message import EmailMessage
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            msg = EmailMessage()
            s.login(" ------ ", ' ---- ')#Enter your gmail and password here
            SUBJECT = "Thank You for shopping with us"
            TEXT = f"Hello {request.user.username},\nYou have been charged Rs.{money}\n For {item} \nWe will deliver your items within 7 working days\n\nThank You for Shopping\nAllStores by Ayush Jain"
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            s.sendmail(" ------ ", f"{email}", message)#Enter your gmail and password here
            s.quit()

            c.save()
            messages.info(request, "Thank you for Ordering")
            return redirect('/products/products')
    else:
        return HttpResponse("Something went wrong Please retry")


def order_details(request):
    order = Order.objects.all()
    print(f"\n\n\n\n\t\t\torder\n\n\n")
    return render(request, "order_details.html", {'order':order})


def back(request):
    return redirect('/')