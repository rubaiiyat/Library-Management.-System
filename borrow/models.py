from django.db import models
from django.contrib.auth.models import User
from books.models import AddBooksModel
# Create your models here.
class BorrowBookModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    book=models.ForeignKey(AddBooksModel, on_delete=models.CASCADE,null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    orginal_id=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.user.username