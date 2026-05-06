from django.shortcuts import redirect, render
from django.views.generic import CreateView, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from userAuth.forms import LoginForm, RegisterForm
from userAuth.models import RegisterModel
from django.contrib.auth import login,logout

class Register(FormView):
    template_name='form.html'
    form_class=RegisterForm
    success_url=reverse_lazy('login')

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
    

class UserLogin(FormView):
    template_name='form.html'
    form_class=LoginForm
    success_url=reverse_lazy('profile')

    def form_valid(self, form):
        user=form.get_user()
        login(self.request,user)
        messages.success(self.request,'Login successful')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["page"] = 'LOGIN'
        return context
    

    
def userLogout(request):
    logout(request)
    messages.success(request,'Successfully Logged Out')
    return redirect('user_login')
    
    