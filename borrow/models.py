from django.db import models
from django.contrib.auth.models import User
from books.models import AddBooksModel
# Create your models here.
class BorrowBookModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    book=models.ManyToManyField(AddBooksModel)

    def __str__(self):
        return self.user.username