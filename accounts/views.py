from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class UserProfile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["page"] = f'Profile'
        return context