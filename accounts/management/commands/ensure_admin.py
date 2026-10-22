
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create a production admin account if missing"

    def handle(self, *args, **options):
        username = os.environ.get("ADMIN_USERNAME")
        password = os.environ.get("ADMIN_PASSWORD")

        if not username or not password:
            raise CommandError(
                "ADMIN_USERNAME and ADMIN_PASSWORD are required."
            )

        User = get_user_model()

        user, created = User.objects.get_or_create(
            username=username
        )

        if created:
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True
            user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    "Production admin created successfully."
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Admin username already exists. "
                    "Password was not changed."
                )
            )
