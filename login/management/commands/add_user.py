"""Create some users."""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


class Command(BaseCommand):
    """Command class."""

    help = "Create some users"

    def handle(self, *args, **options):
        """Main method."""
        User = get_user_model()
        try:
            User.objects.create_superuser("bob", "foo@example.com", "pass")
            self.stdout.write(self.style.SUCCESS("Successfully created bob !"))
        except IntegrityError:
            self.stdout.write(self.style.WARNING("Bob already exists !"))
