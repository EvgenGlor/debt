from rest_framework.serializers import ModelSerializer

from debtlist.models import Debt


class DebtSerializer(ModelSerializer):
    class Meta:
        model = Debt
        fields = '__all__'


