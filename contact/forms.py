from django.core.exceptions import ValidationError
from django import forms
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a class-b',
                'placeholder': 'aqui veio do init',
            }
        ),
        label='primeiro nome',
        help_text='texto de ajuda para usuario',
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a class-b',
        #     'placeholder': 'aqui veio do init',
        # })
    
    
    
    class Meta:
        model = models.Contact
        fields = [
            'first_name', 'last_name', 'phone'
            ]
    
    def clean(self):
        # cleaned_data = self.cleaned_data
        
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid',
            )
        )
        
        return super().clean()