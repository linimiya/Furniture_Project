from django.urls import path
from AdminApp import views

urlpatterns = [
    path('addcategorypagefun/',views.addcategorypagefun,name='addcategorypagefun'),
    path('indexpagefun/',views.indexpagefun,name='indexpagefun'),
    path('Category_DB_Savefun/',views.Category_DB_Savefun,name='Category_DB_Savefun'),
    path('displaycategoryfun/',views.displaycategoryfun,name='displaycategoryfun'),
    path('editcategorypagefun/<int:erow_id>/',views.editcategorypagefun,name='editcategorypagefun'),
    path('update_Category_DBfromEdit/<int:eupd_id>/',views.update_Category_DBfromEdit,name='update_Category_DBfromEdit'),
    path('delete_CategoryDB/<int:del_id>/',views.delete_CategoryDB,name='delete_CategoryDB'),
    path('addproductpagefun/',views.addproductpagefun,name='addproductpagefun'),
    path('Product_DBSavefun/',views.Product_DBSavefun,name='Product_DBSavefun'),
    path('displayproductspagefun/',views.displayproductspagefun,name='displayproductspagefun'),
    path('editproductpagefun/<int:prow_id>/',views.editproductpagefun,name='editproductpagefun'),
    path('update_EditProduct/<int:e_id>/',views.update_EditProduct,name='update_EditProduct'),
    path('loginpagefun/',views.loginpagefun,name='loginpagefun'),
    path('Adminlogin_checkingfun/',views.Adminlogin_checkingfun,name='Adminlogin_checkingfun'),
    path('Admin_logout/',views.Admin_logout,name='Admin_logout'),
    path('Add_blog/',views.Add_blog,name='Add_blog'),
    path('save_Blog_DB/',views.save_Blog_DB,name='save_Blog_DB'),
    path('display_blog/',views.display_blog,name='display_blog')







]
