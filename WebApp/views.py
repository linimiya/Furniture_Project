from django.shortcuts import render, redirect
from AdminApp.models import Product_DB, Category_DB
from WebApp.models import Contact_DB, signup_DB, signup_DB, CartDb, OrderDB
from django.contrib import messages
import razorpay


def home(request):
    homcatobj = Category_DB.objects.all()
    cartobj1 = CartDb.objects.filter(Username=request.session['Name'])
    count = cartobj1.count()

    return render(request, 'Home.html', {'homcatobj': homcatobj, 'count': count})


def product_page(request):
    product = Product_DB.objects.all()
    cartobj1 = CartDb.objects.filter(Username=request.session['Name'])
    count = cartobj1.count()
    return render(request, 'Products.html', {'product': product, 'count': count})


def Aboutus_page(request):
    x = CartDb.objects.all()
    count = x.count()
    return render(request, 'Aboutus.html', {'count': count})


def Contact_page(request):
    return render(request, 'Contact.html')


def Update_Contact(request):
    if request.method == 'POST':
        ca = request.POST.get('tname')

        cd = request.POST.get('temail')
        ce = request.POST.get('textarea')
        obj = Contact_DB(Name=ca, Email=cd, Message=ce)
        obj.save()
        return redirect(Contact_page)


# def delete_contact(request, del_id):
#     x = Product_DB.objects.filter(id=del_id)
#     x.delete()
#     return redirect(contact_data_page)


def product_filtered_page(request, cat_name):
    data = Product_DB.objects.filter(Category_Name=cat_name)
    return render(request, 'product_filtered.html', {'data': data})


def Single_Product_page(request, prod_id):
    data = Product_DB.objects.get(id=prod_id)
    return render(request, 'Single_Product.html', {'data': data})


def Blogs_page(request):
    return render(request, 'Blogs.html')


def Login_page(request):
    return render(request, 'Login.html')


def signup_page1(request):
    return render(request, 'signup.html')


def signup_DB_Save(request):
    if request.method == 'POST':
        sa = request.POST.get('name')
        sb = request.POST.get('email')

        sc = request.POST.get('Mob')
        se = request.POST.get('pass')
        sf = request.POST.get('re_pass')
        signupObj = signup_DB(Name=sa, Email=sb, Mobile=sc, Password=se, ConfirmPassword=sf)
        if signup_DB.objects.filter(Name=sa).exists():
            messages.warning(request, "user already exists..!!")
            return redirect(signup_page1)
        elif signup_DB.objects.filter(Email=sb).exists():
            messages.warning(request, "Email already exists..!!")
            return redirect(signup_page1)

        signupObj.save()
        messages.success(request, 'Registered the user ')
        return redirect(signup_page1)


def user_login(request):
    if request.method == "POST":
        un = request.POST.get('name')  # log in
        pwd = request.POST.get('pass')
        if signup_DB.objects.filter(Name=un, Password=pwd).exists():

            request.session['Name'] = un
            request.session['Password'] = pwd
            messages.success(request, "welcome!..")
            return redirect(home)
        else:
            messages.error(request, "please check your password")
            return redirect(Login_page)
    else:
        messages.warning(request, "Invalid username")
        return redirect(Login_page)


def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(home)


def Cart_DB_save(request):
    if request.method == "POST":
        ca = request.POST.get('tno')
        ac = request.POST.get('titemprice')
        ad = request.POST.get('totprice')
        ae = request.POST.get('tsessionname')
        af = request.POST.get('tproductname')
        try:
            x = Product_DB.objects.get(Product_Name=af)
            img = x.Product_Image1
        except Product_DB.DoesNotExist:
            img = None

        carobj = CartDb(Username=ae, ProductName=af, Quantity=ca, TotalPrice=ad, PricePerItem=ac, Prod_Img=img)
        carobj.save()
        messages.success(request, "your product is saved to cart")
        return redirect(home)


def cart_pagefun(request):
    cartobj1 = CartDb.objects.filter(Username=request.session['Name'])
    subtotal = 0
    Shipping_amount = 0
    total_amount = 0
    for i in cartobj1:
        subtotal = subtotal + i.TotalPrice
    if subtotal > 10000:
        Shipping_amount = 100
    else:
        Shipping_amount = 250
    total_amount = Shipping_amount + subtotal

    return render(request, 'cart.html', {'cartobj1': cartobj1, 'subtotal': subtotal, 'Shipping_amount': Shipping_amount,
                                         'total_amount': total_amount})


def cart_delete(request, d_id):
    x = CartDb.objects.filter(id=d_id)
    x.delete()
    return redirect(cart_pagefun)


def checkout(request):
    cartobj2 = CartDb.objects.filter(Username=request.session['Name'])
    subtotal = 0
    total_amount = 0
    for i in cartobj2:
        subtotal = subtotal + i.TotalPrice
    if subtotal > 10000:
        Shipping_amount = 100
    else:
        Shipping_amount = 250
    total_amount = Shipping_amount + subtotal

    return render(request, 'Checkout.html', {'cartobj2': cartobj2, 'subtotal': subtotal, 'total_amount': total_amount,
                                             'Shipping_amount': Shipping_amount})


def Order_DB_save(request):
    if request.method == "POST":
        oa = request.POST.get('c_fname')
        ob = request.POST.get('c_email')
        oc = request.POST.get('c_place')
        ad = request.POST.get('c_address')
        ae = request.POST.get('c_Mobile')
        af = request.POST.get('cmessage')
        at = request.POST.get('c_total')

        Orderobj = OrderDB(Name=oa, Email=ob, Place=oc, Address=ad, Mobile=ae, Message=af, TotalPrice=at)
        Orderobj.save()
        return redirect(payment_pagefun)


def payment_pagefun(request):
    # retrivedatafrom orderdb with specified id
    customer = OrderDB.objects.order_by('-id').first()

    # get payment amount of specific customer

    payy = customer.TotalPrice
    # convert the amount into paisa- small unit
    amount = int(payy * 100)  # assuming payment amount in rupees

    payy_str = str(amount)

    # to print in console beow line not required
    for i in payy_str:
        print(i)
    if request.method == "POST":
        order_currency = "INR"
        client = razorpay.Client(auth=('rzp_test_QTazbZdC0vhYg3', 'dVtHxomtAL4THQWFXuezm5eG'))
        payment = client.order.create({'amount': amount, 'currency': order_currency})
    return render(request, 'payment_page.html', {'customer': customer, 'payy_str': payy_str})
