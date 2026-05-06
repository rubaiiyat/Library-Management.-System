from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["page"] = 'HOME'
        return context
    

class About(TemplateView):
    template_name='about.html'
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["page"] = 'ABOUT'
        return context
    
class Contact(TemplateView):
    template_name='contact.html'
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["page"] = 'CONTACT'
        return context
    

    