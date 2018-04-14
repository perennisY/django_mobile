from django.urls import path
from . import views


urlpatterns = [
    path('', views.order),
    path('addorder/', views.order_handle),
    path('pay&<int:oid>/', views.pay),
]