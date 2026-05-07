from django.urls import path
from .import views
urlpatterns = [
    path('borrow/<int:id>/', views.BorrowBook.as_view(), name='borrow_book'),
]
