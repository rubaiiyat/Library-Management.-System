from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import AddBooksModel
# Create your views here.

""" class Books(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["books"] = AddBooksModel.objects.all()
        return context """
    

    
