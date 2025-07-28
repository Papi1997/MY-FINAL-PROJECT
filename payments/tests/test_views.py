from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Payee, Payment

class PaymentViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.payee = Payee.objects.create(name='Test Payee', account_number='1234567890')
        self.payment = Payment.objects.create(payee=self.payee, amount='100.00', currency='USD')

    def test_create_payment_view(self):
        response = self.client.get(reverse('create_payment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/create_payment.html')

    def test_payment_list_view(self):
        response = self.client.get(reverse('payment_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.payment.amount)

    def test_payee_list_view(self):
        response = self.client.get(reverse('payee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.payee.name)

    def test_add_payee_view(self):
        response = self.client.post(reverse('add_payee'), {'name': 'New Payee', 'account_number': '1122334455', 'savings_balance': 0, 'loan_limit': 0})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Payee.objects.filter(name='New Payee').exists())

    def test_edit_payee_view(self):
        response = self.client.post(reverse('edit_payee', args=[self.payee.pk]), {'name': 'Updated Payee', 'account_number': self.payee.account_number, 'savings_balance': self.payee.savings_balance, 'loan_limit': self.payee.loan_limit})
        self.assertEqual(response.status_code, 302)
        self.payee.refresh_from_db()
        self.assertEqual(self.payee.name, 'Updated Payee')

    def test_payee_statement_view(self):
        response = self.client.get(reverse('payee_statement', args=[self.payee.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/payee_statement.html')
        self.assertContains(response, self.payment.amount)

    def test_payment_analytics_view(self):
        response = self.client.get(reverse('payment_analytics'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/payment_analytics.html')
        self.assertContains(response, 'Total Payments')

    def test_search_payment(self):
        Payment.objects.create(payee=self.payee, amount='300.00', currency='GBP', status='Completed')
        response = self.client.get(reverse('payment_list'), {'q': 'Completed'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '300.00')
        self.assertNotContains(response, '100.00')

    def test_update_payment_status(self):
        response = self.client.get(reverse('update_payment_status', args=[self.payment.pk, 'Completed']))
        self.assertEqual(response.status_code, 302)
        self.payment.refresh_from_db()
        self.assertEqual(self.payment.status, 'Completed')

    def test_payee_details_display(self):
        self.payee.savings_balance = 1000
        self.payee.loan_limit = 5000
        self.payee.save()
        response = self.client.get(reverse('payee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1000')
        self.assertContains(response, '5000')
