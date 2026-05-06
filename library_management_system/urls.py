
from django.contrib import admin
from django.urls import path
from .views import Home,About,Contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(),name='home'),
    path('about/', About.as_view(),name='about'),
    path('contact/', Contact.as_view(),name='contact'),
]
