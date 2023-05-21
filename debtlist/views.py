from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Debt
from .models import MoneyGiver
from .serializers import (DebtSerializer,
                          MoneyGiverSerializer,
                          DebtInputSerializer,
                          DebtUpdateSerializer, MoneyGiverUpdateSerializer)


class DebtView(ModelViewSet):
    queryset = Debt.objects.all()
    filter_backends = [DjangoFilterBackend, ]

    def get_queryset(self):
        debt_sum = self.request.query_params.get("debt_sum")
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
            return DebtUpdateSerializer
        else:
            raise MethodNotAllowed(self.request.method)

    def patch(self, request, *args, **kwargs):
        initial_data = request.data
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=initial_data)
        serializer.is_valid(raise_exception=True)

        debt = Debt.objects.get(pk=serializer.data["id"])
        debt.debt_sum = serializer.data["debt_sum"]
        debt.save()
        return Response(DebtSerializer(debt).data)


class MoneyGiverView(ModelViewSet):
    queryset = MoneyGiver.objects.all()
    serializer_class = MoneyGiverSerializer
    filter_backends = [DjangoFilterBackend, ]

    def get_queryset(self):
        phone_number = self.request.query_params.get("phone_number")
        queryset = MoneyGiver.objects.all()
        if phone_number:
            queryset = queryset.filter(phone_number=phone_number)

        return queryset

    def get_serializer_class(self):
        if self.request.method in ("GET", "POST"):
            return MoneyGiverSerializer
        elif self.request.method == "PATCH":
            return MoneyGiverUpdateSerializer
        else:
            raise MethodNotAllowed(self.request.method)

    def patch(self, request, *args, **kwargs):
        initial_data = request.data
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=initial_data)
        serializer.is_valid(raise_exception=True)

        money_giver = MoneyGiver.objects.get(pk=serializer.data["id"])
        money_giver.phone_number = serializer.data["phone_number"]
        money_giver.save()
        return Response(MoneyGiverSerializer(money_giver).data)
