from django.urls import path
from auction import views

urlpatterns = [

    path('login', views.userlogin, name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('changepassword', views.changepassword, name = 'changepassword'),

    path('', views.home, name = 'home'),
    path('auctionstart', views.auctionstart, name = 'auctionstart'),
]