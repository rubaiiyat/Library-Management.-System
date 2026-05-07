from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.contrib import messages

from books.models import AddBooksModel
from borrow.models import BorrowBookModel
# Create your views here.

class BorrowBook(View):
    def get(self, request, id):
        book=AddBooksModel.objects.get(pk=id)

        borrow_obj,created=BorrowBookModel.objects.get_or_create(
            user=self.request.user
        )

        if borrow_obj.book.filter(id=book.id).exists():
            messages.warning(request,'You have already borrowd this book')
            return redirect('book_detail', slug=book.slug)
        
        borrow_obj.book.add(book)

        book.available_copies-=1
        book.save()

        messages.success(request, "Book borrowed successfully")

        return redirect('profile')