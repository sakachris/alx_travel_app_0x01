from django.core.management.base import BaseCommand
from listings.models import Property, User
from django.utils import timezone
from decimal import Decimal
import uuid

class Command(BaseCommand):
    help = 'Seed the database with sample property data'

    def handle(self, *args, **kwargs):
        # Create or get host user
        host, created = User.objects.get_or_create(
            email='host@example.com',
            defaults={
                'first_name': 'Host',
                'last_name': 'User',
                'role': 'host',
                'password_hash': 'dummyhashed',
            }
        )

        # Create sample properties
        for i in range(5):
            Property.objects.create(
                host=host,
                name=f"Sample Property {i+1}",
                description="A lovely place to stay.",
                location="Nairobi",
                pricepernight=Decimal("99.99"),
            )

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings."))
