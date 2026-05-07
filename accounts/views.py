from django.shortcuts import render
from django.views.generic import TemplateView

from userAuth.models import RegisterModel
from balance.models import BalanceModel
# Create your views here.
class UserProfile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        user=self.request.user
        register=RegisterModel.objects.filter(user=user).first()
        balance=BalanceModel.objects.filter(user=user).first()
        context["user"] = user
        context["page"] = f'Profile'
        context["register"] = register
        context["balance"] = balance
        
        return context