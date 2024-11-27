from django.urls import path
from WebApp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product_page/', views.product_page, name='product_page'),
    path('Aboutus_page/', views.Aboutus_page, name='Aboutus_page'),
    path('Contact_page/', views.Contact_page, name='Contact_page'),
    path('Update_Contact/', views.Update_Contact, name='Update_Contact'),
    # path('contact_data_page/', views.contact_data_page, name='contact_data_page'),
    # path('delete_contact/<int:del_id>/', views.delete_contact, name='delete_contact'),
    path('product_filtered_page/<cat_name>/', views.product_filtered_page, name='product_filtered_page'),
    path('Single_Product_page/<int:prod_id>', views.Single_Product_page, name='Single_Product_page'),
    path('Blogs_page/', views.Blogs_page, name='Blogs_page'),
    path('', views.Login_page, name='Login_page'),
    path('signup_page1/', views.signup_page1, name='signup_page1'),
    path('signup_DB_Save/', views.signup_DB_Save, name='signup_DB_Save'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('Cart_DB_save/', views.Cart_DB_save, name='Cart_DB_save'),
    path('cart_pagefun/',views.cart_pagefun,name='cart_pagefun'),
    path('cart_delete/<int:d_id>',views.cart_delete,name='cart_delete'),
    path('checkout/',views.checkout,name='checkout'),
    path('Order_DB_save/',views.Order_DB_save,name='Order_DB_save'),
    path('payment_pagefun/',views.payment_pagefun,name='payment_pagefun')

]
