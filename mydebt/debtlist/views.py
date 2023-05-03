from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import Debt
from .models import MoneyGiver
from .serializers import DebtSerializer, MoneyGiverSerializer


class DebtView(ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    filter_backends = [DjangoFilterBackend, ]

    # def get_queryset(self):
    #     debt_sum = self.request.query_params.get('debt_sum')
    #     return Debt.objects.all().filter(debt_sum=debt_sum)

    def get_queryset(self):
        debt_sum = self.request.query_params.get("debt_sum", None)
        queryset = Debt.objects.all()
        if debt_sum:
            queryset = queryset.filter(debt_sum=debt_sum)

        return queryset


class MoneyGiverView(ModelViewSet):
    queryset = MoneyGiver.objects.all()
    serializer_class = MoneyGiverSerializer
    filter_backends = [DjangoFilterBackend, ]