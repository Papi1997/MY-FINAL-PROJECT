from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment, Payee
from .forms import PaymentForm, PayeeForm

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

def payee_list(request):
    payees = Payee.objects.all()
    return render(request, 'payments/payee_list.html', {'payees': payees})

def add_payee(request):
    if request.method == 'POST':
        form = PayeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payee_list')
    else:
        form = PayeeForm()
    return render(request, 'payments/add_payee.html', {'form': form})

def edit_payee(request, pk):
    payee = get_object_or_404(Payee, pk=pk)
    if request.method == 'POST':
        form = PayeeForm(request.POST, instance=payee)
        if form.is_valid():
            form.save()
            return redirect('payee_list')
    else:
        form = PayeeForm(instance=payee)
    return render(request, 'payments/edit_payee.html', {'form': form})

def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'payments/payment_detail.html', {'payment': payment})
