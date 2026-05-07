from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from balance.models import BalanceModel
from balance.forms import BalanceForm
# Create your views here.


class BalanceCreateView(CreateView):
    model = BalanceModel
    template_name ="form.html"
    form_class=BalanceForm
    success_url=reverse_lazy('profile')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page']='ADD BALANCE'
        return context
    
    def form_valid(self, form):
        amount=form.cleaned_data['balance']
        current_obj,created=self.model.objects.get_or_create(
            user=self.request.user,
            defaults={'balance':0}
        )
        
        current_obj.balance+=amount
        current_obj.save()
        form.instance.user=self.request.user
        messages.success(self.request,f'You have deposit {amount}Tk. Your current balance is {current_obj.balance}Tk')
        return redirect(self.success_url)
    
