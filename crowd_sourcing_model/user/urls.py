from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'balance', views.user),
    url(r'login',views.login),
]