from django.db import models


class MoneyGiver(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=30)
    phone_number = models.IntegerField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return str(self.name)


class Debt(models.Model):
    class Meta:
        ordering = ['money_giver']  # для упорядочивания

    money_giver = models.ForeignKey(to=MoneyGiver, to_field="id", on_delete=models.PROTECT, related_name="debt")
    debt_sum = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    @property
    def notes_short(self) -> str:
        if len(self.notes) < 48:
            return self.notes
        return self.notes[:48] + '...'

    def __str__(self) -> str:
        return str(self.money_giver.__str__())
