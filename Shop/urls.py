
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('products/', include('products.urls') ,name='products'),
    path('accounts/', include("accounts.urls"),name='accounts'),
]
