from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from debtlist.models import Debt, MoneyGiver


class DebtInputSerializer(ModelSerializer):
    class Meta:
        model = Debt
        fields = "__all__"


class DebtSerializer(ModelSerializer):
    class Meta:
        model = Debt
        fields = (
            "id",
            "name",
            "debt_sum",
            "notes",
            "phone_number",
        )

    name = ReadOnlyField(source="money_giver.name")
    phone_number = ReadOnlyField(source="money_giver.phone_number")


class MoneyGiverSerializer(ModelSerializer):
    class Meta:
        model = MoneyGiver
        fields = '__all__'
