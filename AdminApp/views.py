from django.shortcuts import render, redirect
from AdminApp.models import Category_DB, Product_DB, Blog_DB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.contrib import messages


def addcategorypagefun(res):
    return render(res, 'AddCategory.html')


# Create your views here.

def indexpagefun(res):
    today_date = datetime.now()

    count_cat = Category_DB.objects.count()
    count_prod = Product_DB.objects.count()
    return render(res, 'index.html', {'today_date': today_date, 'count_cat': count_cat, 'count_prod': count_prod})


def Category_DB_Savefun(request):
    if request.method == 'POST':
        ca = request.POST.get('tcatname')
        cb = request.POST.get('tcatdesc')
        cc = request.FILES['timg']
        obj = Category_DB(Category_Name=ca, Category_Description=cb, Category_Image=cc)
        obj.save()
        messages.success(request, 'Category got saved')

        return redirect(addcategorypagefun)


def displaycategoryfun(res):
    obj1 = Category_DB.objects.all()
    return render(res, 'displaycategory.html', {'obj1': obj1})


def editcategorypagefun(res, erow_id):
    erow_id = Category_DB.objects.get(id=erow_id)
    return render(res, 'editcategory.html', {'erow_id': erow_id})


def update_Category_DBfromEdit(request, eupd_id):
    if request.method == 'POST':
        ea = request.POST.get('tcatname')
        eb = request.POST.get('tcatdesc')
        try:
            cc = request.FILES['timg']
            fs = FileSystemStorage()
            file = fs.save(cc.name, cc)
        except MultiValueDictKeyError:
            file = Category_DB.objects.get(id=eupd_id).Category_Image
        Category_DB.objects.filter(id=eupd_id).update(
            Category_Name=ea,
            Category_Description=eb,
            Category_Image=file

        )
        return redirect(displaycategoryfun)


def delete_CategoryDB(request, del_id):
    x = Category_DB.objects.filter(id=del_id)
    x.delete()
    messages.success(request, "Deleted!!..")
    return redirect(displaycategoryfun)


def addproductpagefun(res):
    cat = Category_DB.objects.all()
    return render(res, 'Addproducts.html', {'cat': cat})


def Product_DBSavefun(request):
    if request.method == 'POST':
        a = request.POST.get('category')
        pa = request.POST.get('tpodname')
        pb = request.POST.get('tpodQuantity')
        pc = request.POST.get('tpodMRP')
        pd = request.POST.get('Description')
        pe = request.POST.get('tpodOrigin')
        pf = request.POST.get('tpodMan')
        pi1 = request.FILES['tpodimg1']
        pi2 = request.FILES['tpodimg2']
        pi3 = request.FILES['tpodimg3']
        obj = Product_DB(Category_Name=a, Product_Name=pa,
                         Product_Quantity=pb,
                         Product_MRP=pc,
                         Product_Description=pd,
                         Product_Country=pe,
                         Product_Manufactured=pf, Product_Image1=pi1, Product_Image2=pi2, Product_Image3=pi3)
        obj.save()
        return redirect(addproductpagefun)


def displayproductspagefun(request):
    obj3 = Product_DB.objects.all()

    return render(request, 'displayproducts.html', {'obj3': obj3})


def editproductpagefun(request, prow_id):
    cat = Category_DB.objects.all()
    pod = Product_DB.objects.get(id=prow_id)

    return render(request, 'editproducts.html', {'cat': cat, 'pod': pod})


def update_EditProduct(request, e_id):
    if request.method == "POST":
        ea = request.POST.get('tpodname')
        eb = request.POST.get('tpodQuantity')
        ec = request.POST.get('tpodMRP')
        ed = request.POST.get('Description')
        ee = request.POST.get('tpodOrigin')
        ef = request.POST.get('tpodMan')
        try:
            im1 = request.FILES['tpodimg1']
            fs = FileSystemStorage()
            file1 = fs.save(im1.name, im1)
        except MultiValueDictKeyError:
            file1 = Product_DB.objects.get(id=e_id).Product_Image1
        try:
            im2 = request.FILES['tpodimg2']
            fs = FileSystemStorage()
            file2 = fs.save(im2.name, im2)

        except MultiValueDictKeyError:
            file2 = Product_DB.objects.get(id=e_id).Product_Image2

        try:
            im3 = request.FILES['tpodimg3']
            fs = FileSystemStorage()
            file3 = fs.save(im3.name, im3)

        except MultiValueDictKeyError:
            file3 = Product_DB.objects.get(id=e_id).Product_Image3
        Product_DB.objects.filter(id=e_id).update(Product_Name=ea, Product_Quantity=eb,
                                                  Product_MRP=ec, Product_Description=ed,
                                                  Product_Country=ee, Product_Manufactured=ef,
                                                  Product_Image1=file1, Product_Image2=file2, Product_Image3=file3)
        return redirect(displayproductspagefun)


def loginpagefun(request):
    return render(request, 'Adminlogin.html')


def Adminlogin_checkingfun(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pswd = request.POST.get('pass')

        if User.objects.filter(username__contains=un).exists():
            mob = authenticate(username=un, password=pswd)
            if mob is not None:
                login(request, mob)
                request.session['username'] = un
                request.session['password'] = pswd
                messages.success(request, "welcome!..")
                return redirect(indexpagefun)
            else:
                messages.error(request, "please check your password")
                return redirect(loginpagefun)
        else:
            messages.warning(request, "Invalid username")
            return redirect(loginpagefun)


def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.info(request, "Logged out successfully")

    return redirect(loginpagefun)


def Add_blog(request):
    return render(request, 'Add_blog.html')


def save_Blog_DB(request):
    if request.method == 'POST':
        ba = request.POST.get('tblogdet')
        bb = request.FILES['tnlogimg']
        objBlog = Blog_DB(Blog_Data=ba, Blog_Image=bb)
        objBlog.save()
        return redirect(Add_blog)


def display_blog(request):
    datablog = Blog_DB.objects.all()

    return render(request, 'display_blog.html', {'datablog': datablog})
