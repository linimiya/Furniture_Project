from django.db import models
class Category_DB(models.Model):
    Category_Name=models.CharField(max_length=100,blank=True,null=True)
    Category_Description=models.CharField(max_length=100,blank=True,null=True)
    Category_Image=models.ImageField(upload_to="catimg",blank=True,null=True)



# Create your models here.
class Product_DB(models.Model):
    Category_Name = models.CharField(max_length=100, blank=True, null=True)
    Product_Name=models.CharField(max_length=100,blank=True,null=True)
    Product_Quantity=models.IntegerField(blank=True,null=True)
    Product_MRP=models.IntegerField(blank=True,null=True)
    Product_Description=models.CharField(max_length=100,blank=True,null=True)
    Product_Country=models.CharField(max_length=100,blank=True,null=True)
    Product_Manufactured=models.CharField(max_length=100,blank=True,null=True)
    Product_Image1=models.ImageField(upload_to="prodimg",blank=True,null=True)
    Product_Image2 = models.ImageField(upload_to="prodimg", blank=True, null=True)
    Product_Image3 = models.ImageField(upload_to="prodimg", blank=True, null=True)

class Blog_DB(models.Model):
    Blog_Data=models.CharField(max_length=100,blank=True,null=True)
    Blog_Image=models.ImageField(upload_to="blogimg",blank=True,null=True)



