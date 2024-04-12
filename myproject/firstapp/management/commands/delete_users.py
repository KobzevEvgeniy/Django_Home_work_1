from django.core.management.base import BaseCommand

from myproject.firstapp.models import User


class Command(BaseCommand):
    help = "Delete users"


def handle(self, user_id):
    if user_id == User.indexes:
        User.delete()
    self.stdout.write(f'user with {user_id} delete successfully')
