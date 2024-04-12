from django.core.management.base import BaseCommand

from myproject.firstapp.models import User


class Command(BaseCommand):
    help = "Update users"


def handle(self, user_id,*args, **kwargs):
    if user_id == User.indexes:
        User._do_update()
    self.stdout.write(f'user with {user_id} delete successfully')
