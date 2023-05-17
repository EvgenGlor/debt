from rest_framework.exceptions import ValidationError
from rest_framework.fields import ReadOnlyField, IntegerField, FloatField
from rest_framework.serializers import ModelSerializer, Serializer

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


    # def validate_debt_sum(self, obj):
    #     if obj
class DebtUpdateSerializer(Serializer):
    id = IntegerField()
    debt_sum = FloatField(min_value=10, max_value=1000000)

    def validate_id(self, attr):
        try:
            debt = Debt.objects.get(pk=attr)
        except Debt.DoesNotExist:
            raise ValidationError(detail="Не существует сущности Debt с идентификатором {}".format(attr))
        return attr




class MoneyGiverSerializer(ModelSerializer):
    class Meta:
        model = MoneyGiver
        fields = '__all__'
