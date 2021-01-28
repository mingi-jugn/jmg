from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns=[

    path('index/',views.index, name='index'),
    path('index1/', views.index1, name='index1'),
    path('product/', views.product, name='product'),
    path('showindex/', views.showindex, name='showindex'),
   path('showdetail/<subject>', views.showdetail, name='showdetail'),
    path('', views.sample1, name='sample1'),
    path('album/', views.album, name='album'),





]