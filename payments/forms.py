from django import forms
from .models import Payment, Payee

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payee', 'amount']

class PayeeForm(forms.ModelForm):
    class Meta:
        model = Payee
        fields = ['name', 'account_number']
