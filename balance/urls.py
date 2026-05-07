from django.urls import path
from .import views
urlpatterns = [
    path('add/',views.BalanceCreateView.as_view(),name='add_balance')    
]
