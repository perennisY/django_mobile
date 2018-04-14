from django.urls import path

from . import views

app_name = 'df_user'
urlpatterns=[
    path('register/',views.register,name='register'),
    path('register_handle/',views.register_handle,name='register_handle'),
    path('register_exist/',views.register_exist),
    path('login_handle/',views.login_handle),
    path('login/',views.login),
    path('info/',views.info),
    path('site/',views.site),
    path('logout/',views.logout),
    path('user_center_order&<int:pageid>/',views.user_center_order),
]