from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payments/create_payment.html', {'form': form})

def payment_list(request):
    payments = Payment.objects.all().order_by('-created_at')
    return render(request, 'payments/payment_list.html', {'payments': payments})
