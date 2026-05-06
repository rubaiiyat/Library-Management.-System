from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.Register.as_view(),name='register'),
    path('login/',views.UserLogin.as_view(),name='user_login'),
    path('logout/',views.userLogout,name='user_logout'),
]
