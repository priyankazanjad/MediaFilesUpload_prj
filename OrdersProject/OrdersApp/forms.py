from django import forms
from .models import Orders

class OrdersModelForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        labels = {
            'company':'Enter company name',
            'model_name':'Enter laptop name',
            'ram':'Enter ram',
            'rom':'Enter rom',
        }
        widgets = {
            'ram':forms.TextInput(attrs={'palceholder':'in GB'}),
            'rom':forms.TextInput(attrs={'palceholder':'in GB'}),
        }
    def clean_ram(self):
        ram = self.cleaned_data['ram']
        if ram<=0:
            raise forms.ValidationError('ram must be greater than zero')
        elif ram % 2 !=0:
            raise forms.ValidationError('ram must be even number')
        else:
            return ram

    def clean_rom(self):
        rom = self.cleaned_data['rom']
        if rom<=0:
            raise forms.ValidationError("rom must be greater than zero")
        else:
            return rom