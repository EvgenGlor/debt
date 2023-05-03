from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Debt
from .models import MoneyGiver
from .serializers import DebtSerializer, MoneyGiverSerializer, DebtInputSerializer


class DebtView(ModelViewSet):
    queryset = Debt.objects.all()
    filter_backends = [DjangoFilterBackend, ]

    def get_queryset(self):
        debt_sum = self.request.query_params.get("debt_sum", None)
        queryset = Debt.objects.all()
        if debt_sum:
            queryset = queryset.filter(debt_sum=debt_sum)

        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DebtSerializer
        elif self.request.method == "POST":
            return DebtInputSerializer
        elif self.request.method == "PATCH":
            return DebtSerializer
        else:
            raise MethodNotAllowed(self.request.method)

    def patch(self, request):
        debt_id = request.data.get("id")
        debt_sum = request.data.get("debt_sum")
        debt = Debt.objects.get(pk=debt_id)
        debt.debt_sum = debt_sum
        debt.save()
        serializer = self.get_serializer_class()
        return Response(data=serializer(debt).data)







class MoneyGiverView(ModelViewSet):
    queryset = MoneyGiver.objects.all()
    serializer_class = MoneyGiverSerializer
    filter_backends = [DjangoFilterBackend, ]