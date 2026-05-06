from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .constants import CHOICE_DEPARTMENT
from django.contrib.auth.views import LoginView

class RegisterForm(UserCreationForm):
    id_card_number=forms.CharField(min_length=5,max_length=5, required=True)
    department=forms.ChoiceField(choices=CHOICE_DEPARTMENT, required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','id_card_number','department']
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({
                'class':'input w-full'
            })
    

class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class':'input w-full'
            })
        