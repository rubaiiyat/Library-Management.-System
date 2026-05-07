from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View

from userAuth.models import RegisterModel
from balance.models import BalanceModel
from borrow.models import BorrowBookModel
from books.models import AddBooksModel
# Create your views here.
class UserProfile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        user=self.request.user
        register=RegisterModel.objects.filter(user=user).first()
        balance=BalanceModel.objects.filter(user=user).first()
        borrow=BorrowBookModel.objects.filter(user=user)
        context["user"] = user
        context["page"] = f'Profile'
        context["register"] = register
        context["balance"] = balance
        context['borrow']=borrow
        
        return context
    
class BackBook(View):

    def get(self,request,id):
        book=BorrowBookModel.objects.get(pk=id)
        addBook=AddBooksModel.objects.get(pk=book.orginal_id)
        balance_obj,created=BalanceModel.objects.get_or_create(
            user=request.user
        )

        balance_obj.balance+=book.book.price
        balance_obj.save()
        book.book.available_copies+=1
        addBook.available_copies+=1
        addBook.save()
        book.delete()

        return redirect('profile')
