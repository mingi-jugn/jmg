from django.db import models
from django.views.generic import ListView


class Test(models.Model):
    subject=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images' ,blank=True)
    summary=models.TextField(max_length=500, help_text="설명을 적으시오")
    upload_date = models.DateField(null=True,blank=True)
    acount=models.CharField(max_length=1)
    def __str__(self):
        return self.subject


class Product(models.Model):
    subject=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    upload_date = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    categories = models.ManyToManyField('Category',related_name='posts')
    def __str__(self):
        return self.subject

class ProductList(ListView):
    paginate_by=5
    model = Product



class Pcomment(models.Model):
    name= models.CharField(max_length=20)
    content = models.TextField(max_length=300,null=True)
    make_date=models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE)



class Category(models.Model):
    name = models.CharField(max_length=20)

