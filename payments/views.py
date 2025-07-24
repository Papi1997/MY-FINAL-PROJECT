from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment, Payee
from .forms import PaymentForm, PayeeForm
from django.contrib.auth.decorators import login_required

@login_required
def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            return render(request, 'payments/payment_confirmation.html', {'payment': payment})
    else:
        form = PaymentForm()
    return render(request, 'payments/create_payment.html', {'form': form})

from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def payment_list(request):
    query = request.GET.get('q')
    if query:
        payments = Payment.objects.filter(
            Q(payee__name__icontains=query) |
            Q(amount__icontains=query) |
            Q(status__icontains=query)
        ).order_by('-created_at')
    else:
        payments = Payment.objects.all().order_by('-created_at')
    return render(request, 'payments/payment_list.html', {'payments': payments})

from django.contrib.auth.decorators import login_required

@login_required
def payee_list(request):
    payees = Payee.objects.all()
    return render(request, 'payments/payee_list.html', {'payees': payees})

@login_required
def add_payee(request):
    if request.method == 'POST':
        form = PayeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payee_list')
    else:
        form = PayeeForm()
    return render(request, 'payments/add_payee.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
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

from django.contrib.auth.decorators import login_required

@login_required
def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'payments/payment_detail.html', {'payment': payment})

def confirm_payment(request):
    if request.method == 'POST':
        payee_id = request.POST['payee']
        payee = get_object_or_404(Payee, pk=payee_id)
        payment = Payment.objects.create(
            payee=payee,
            amount=request.POST['amount'],
            currency=request.POST['currency'],
        )
        return redirect('payment_detail', pk=payment.pk)
    return redirect('create_payment')
