from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('web3',views.web3app, name="web3"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")

]