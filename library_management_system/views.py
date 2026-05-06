from django.views.generic import DetailView, TemplateView

from books.models import AddBooksModel

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["page"] = 'HOME'
        context["books"] = AddBooksModel.objects.all()
        return context
    

class BookDetailView(DetailView):
    model = AddBooksModel
    template_name = "book_detail.html"
    context_object_name='book'
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["page"] = self.object.name
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
    

    