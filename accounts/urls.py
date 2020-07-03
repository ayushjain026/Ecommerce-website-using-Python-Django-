from . import views
from django.urls import path


urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("contacts", views.contacts, name="contact"),
    path('lost', views.lost),
    path('reset', views.reset),
    path('s', views.s),
]
