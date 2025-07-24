from django.db import models

class Payee(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Payment(models.Model):
    payee = models.ForeignKey(Payee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
