from django import forms


class AddNewDebt(forms.Form):
    name = forms.CharField()
    debt_sum = forms.DecimalField()
    return_date = forms.DateField()
    take_date = forms.DateField()
    notes = forms.CharField()

