from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.contrib import messages

from books.models import AddBooksModel
from borrow.models import BorrowBookModel
from balance.models import BalanceModel
# Create your views here.

class BorrowBook(View):
    def get(self, request, id):
        book=AddBooksModel.objects.get(pk=id)

        balance_obj,create=BalanceModel.objects.get_or_create(
            user=self.request.user
        )

        if BorrowBookModel.objects.filter(user=self.request.user, book=book).exists():
            messages.warning(request, 'You have already borrowed this book')
            return redirect('book_detail', slug=book.slug)
        
        if balance_obj.balance<book.price:
            messages.warning(request, 'You have not enough money')
            return redirect('book_detail', slug=book.slug)   

        BorrowBookModel.objects.create(
            user=self.request.user,
            book=book,
            orginal_id=book.id
        )

        

        book.available_copies-=1
        balance_obj.balance-=book.price
        book.save()
        balance_obj.save()

        messages.success(request, "Book borrowed successfully")

        return redirect('profile')
    
    