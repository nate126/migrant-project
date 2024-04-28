from django.core.management.base import BaseCommand
from pages.data import get_all_shelters

class Command(BaseCommand):
    help = 'Populates the Location table with data'

    def handle(self, *args, **kwargs):
        get_all_shelters()