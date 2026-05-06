from django.shortcuts import render
from django.views.generic import CreateView,FormView
from django.urls import reverse_lazy
from django.contrib import messages
from userAuth.forms import RegisterForm
from userAuth.models import RegisterModel

class Register(FormView):
    template_name='form.html'
    form_class=RegisterForm
    success_url=reverse_lazy('register')

    def form_valid(self, form):
        user=form.save()
        RegisterModel.objects.create(
            user=user,
            id_card_number=form.cleaned_data['id_card_number'],
            department=form.cleaned_data['department'],
        )

        messages.success(self.request,'Account created successfully')
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["page"] = 'REGISTER'
        return context
    

