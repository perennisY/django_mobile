
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('list<int:typeid>_<int:pageid>_<int:sort>/',views.goodlist),
    path('<int:id>/', views.detail),
]