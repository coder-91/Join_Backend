from django.core.management.base import BaseCommand
from user.models import User
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Delete guest users older than 24 hours.'

    def handle(self, *args, **kwargs):
        cutoff = timezone.now() - timedelta(hours=24)
        guests_to_delete = User.objects.filter(is_guest=True, date_joined__lt=cutoff)
        count = guests_to_delete.count()
        guests_to_delete.delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} guest(s)'))