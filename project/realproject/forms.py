from django import forms
import datetime
from django.forms import SelectDateWidget
from .models import Test, Product, Pcomment

class RstForm(forms.ModelForm):
    subject = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder": "Your Name"
        })
    )
    summary = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder":"Leave a comment!",
                "cols":10, "rows":10
            }
        )
    )
    upload_date=forms.DateField(widget=SelectDateWidget(empty_label="NOTING"))
    image=forms.ImageField()
    METHOD=(
        ('C','cash'),
        ('B','card'),
        ('P','point'),
    )
    acount = forms.CharField(label='What is your bill', widget=forms.Select(choices=METHOD))
    class Meta:
        model = Test
        fields = ('subject','image', 'summary', 'upload_date','acount')




class ProductForm(forms.ModelForm):
    subject = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder": "Food Name"
        })
    )
    price = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "product price"
        })
    )
    upload_date=forms.DateField(widget=SelectDateWidget(empty_label="NOTING"))
    image = forms.ImageField()

    class Meta:
        model = Product
        fields = ('subject','price', 'upload_date','image')

class PcommentForm(forms.ModelForm):
    class Meta:
        model = Pcomment
        fields=('name','content')