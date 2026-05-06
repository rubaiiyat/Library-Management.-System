from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import Home,About,Contact,BookDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(),name='home'),
    path('details/<str:slug>', BookDetailView.as_view(),name='book_detail'),
    path('about/', About.as_view(),name='about'),
    path('contact/', Contact.as_view(),name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)