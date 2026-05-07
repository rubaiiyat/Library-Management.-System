from django.urls import path
from .import views

urlpatterns = [
    path('profile/',views.UserProfile.as_view(),name='profile'),
    path('back/<int:id>',views.BackBook.as_view(),name='back_book')
]
