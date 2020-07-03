from . import views
from django.urls import path


urlpatterns = [
    path('', views.products),
    path('products', views.products),
    path('cart', views.cart, name="cart"),
    path('remove', views.remove, name="remove"),
    path('clear_cart',views.clear_cart),
    path('main',views.main, name='main'),
    path('vegetable',views.vegetable, name='vegetable'),
    path('dal_rice',views.dal_rice, name='vegetable'),
    path('cookie_snack',views.cookie_snack),
    path('checkout',views.checkout),
    path('buy',views.buy),
    path('order_details', views.order_details),
    path('back', views.back, name="back"),
]