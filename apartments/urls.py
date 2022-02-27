from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('checkout/', checkout, name='checkout'),
    path('order/', order, name='order'),
    path('order-cancel/', order_cancel, name='order_cancel'),
    path('all_orders/', all_orders, name='all_orders'),
    path('apartment/<slug>', apart_detal, name='apart'),
]