from django.core.management.base import BaseCommand
from django.utils import timezone
from payments.models import Payment

class Command(BaseCommand):
    help = 'Processes scheduled payments that are due'

    def handle(self, *args, **options):
        now = timezone.now()
        scheduled_payments = Payment.objects.filter(status='Scheduled', scheduled_date__lte=now)

        for payment in scheduled_payments:
            # Here you would add the logic to actually process the payment
            # For now, we'll just update the status to 'Pending'
            payment.status = 'Pending'
            payment.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully processed payment {payment.id}'))

        self.stdout.write(self.style.SUCCESS('Finished processing scheduled payments.'))
