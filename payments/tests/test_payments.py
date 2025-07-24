from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Payee, Payment

class PaymentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.payee = Payee.objects.create(name='Test Payee', account_number='1234567890')

    def test_create_payment(self):
        response = self.client.post(reverse('create_payment'), {
            'payee': self.payee.id,
            'amount': '100.00',
            'currency': 'USD',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/payment_confirmation.html')

    def test_confirm_payment(self):
        response = self.client.post(reverse('confirm_payment'), {
            'payee': self.payee.id,
            'amount': '100.00',
            'currency': 'USD',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Payment.objects.count(), 1)
        payment = Payment.objects.first()
        self.assertEqual(payment.payee, self.payee)
        self.assertEqual(payment.amount, 100.00)
        self.assertEqual(payment.currency, 'USD')

    def test_payment_list(self):
        Payment.objects.create(payee=self.payee, amount='200.00', currency='EUR')
        response = self.client.get(reverse('payment_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '200.00')
        self.assertContains(response, 'EUR')

    def test_search_payment(self):
        Payment.objects.create(payee=self.payee, amount='300.00', currency='GBP', status='Completed')
        response = self.client.get(reverse('payment_list'), {'q': 'Completed'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '300.00')
        self.assertNotContains(response, '100.00')
