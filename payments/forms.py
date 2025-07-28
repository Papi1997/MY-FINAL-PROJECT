from django import forms
from .models import Payment, Payee

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payee', 'amount', 'currency', 'payment_method', 'mpesa_phone_number', 'mpesa_till_number', 'mpesa_paybill_number', 'mpesa_account_reference']
        widgets = {
            'currency': forms.Select(choices=Payment.CURRENCY_CHOICES),
            'payment_method': forms.Select(choices=Payment.PAYMENT_METHOD_CHOICES),
        }

class PayeeForm(forms.ModelForm):
    class Meta:
        model = Payee
        fields = ['name', 'account_number', 'email', 'phone_number', 'id_number', 'postal_address', 'savings_balance', 'loan_limit']
