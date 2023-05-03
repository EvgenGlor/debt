from rest_framework.serializers import ModelSerializer

from debtlist.models import Debt, MoneyGiver


class DebtSerializer(ModelSerializer):
    class Meta:
        model = Debt
        fields = '__all__'


class MoneyGiverSerializer(ModelSerializer):
    class Meta:
        model = MoneyGiver
        fields = '__all__'


