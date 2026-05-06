from django.db import models
from django.contrib.auth.models import User
from .constants import CHOICE_DEPARTMENT

class RegisterModel(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    id_card_number=models.CharField( max_length=5, unique=True)
    department=models.CharField(choices=CHOICE_DEPARTMENT, max_length=50,blank=True,null=True)

    def __str__(self):
        return self.id_card_number
    