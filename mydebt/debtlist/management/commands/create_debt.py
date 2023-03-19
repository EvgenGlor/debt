from django.core.management import BaseCommand
from debtlist.models import Debt


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Добавление новой записи')

        debt_names = [
            'Артур',
            'Сберкредит',
        ]
        for name in debt_names:
            current_name, created = Debt.objects.get_or_create(name=name)
            self.stdout.write(f'Дбавлена запись {current_name.name}')
        self.stdout.write(self.style.SUCCESS('Запись добавлена'))