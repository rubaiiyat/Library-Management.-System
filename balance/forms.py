from django import forms
from balance.models import BalanceModel

class BalanceForm(forms.ModelForm):
    class Meta:
        model=BalanceModel
        fields=['balance']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({
                'class':'input w-full'
            })
    