from django.contrib import admin
from .models import Test,Product

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['id','subject','image','summary','upload_date','acount']
    list_display_links = ['id','subject']

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

