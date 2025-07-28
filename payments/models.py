from django.db import models

class Payee(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    id_number = models.CharField(max_length=20, blank=True, null=True)
    postal_address = models.TextField(blank=True, null=True)
    savings_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    loan_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Card', 'Card'),
        ('B2C', 'B2C (M-Pesa)'),
        ('LipaNaMpesaTill', 'Lipa na M-Pesa (Till)'),
        ('LipaNaMpesaPaybill', 'Lipa na M-Pesa (Paybill)'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
        ('Scheduled', 'Scheduled'),
    ]
    CURRENCY_CHOICES = [
        ('KES', 'Kenyan Shilling'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
    ]
    payee = models.ForeignKey(Payee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='KES')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='Card')
    mpesa_phone_number = models.CharField(max_length=20, blank=True, null=True)
    mpesa_till_number = models.CharField(max_length=20, blank=True, null=True)
    mpesa_paybill_number = models.CharField(max_length=20, blank=True, null=True)
    mpesa_account_reference = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
