from django.db import models


class Debt(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(max_length=30)
    debt_sum = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    return_date = models.DateField(auto_now_add=True)
    take_date = models.DateField(auto_now_add=True)
    notes = models.TextField(null=False, blank=True)

    @property
    def notes_short(self) -> str:
        if len(self.notes) < 48:
            return self.notes
        return self.notes[:48] + '...'

    def __str__(self) -> str:
        return str(self.name) #работает
# Create your models here.

