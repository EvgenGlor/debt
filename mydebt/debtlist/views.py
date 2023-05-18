from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import MethodNotAllowed, ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Debt
from .models import MoneyGiver
from .serializers import DebtSerializer, MoneyGiverSerializer, DebtInputSerializer, DebtUpdateSerializer, \
    MoneyGiverInputSerializer, MoneyGiverUpdateSerializer


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
            return DebtUpdateSerializer
        else:
            raise MethodNotAllowed(self.request.method)

    def patch(self, request, *args, **kwargs):
        initial_data = request.data #Переменная initial_data = всё что находится в body запроса
        serializer_class = self.get_serializer_class() #serializer = обращение к функции get_serializer_class, которая знает, что мы сделали запрос patch
        serializer = serializer_class(data=initial_data)
        serializer.is_valid(raise_exception=True) #Провалидировали body на предмет коректности. ВСЕ ПОЛЯ

        debt = Debt.objects.get(pk=serializer.data["id"]) #objects общение с объектами данной модели
        debt.debt_sum = serializer.data["debt_sum"]
        debt.save()
        return Response(DebtSerializer(debt).data)


class MoneyGiverView(ModelViewSet):
    queryset = MoneyGiver.objects.all()
    filter_backends = [DjangoFilterBackend, ]

    def get_queryset(self):
        debt_sum = self.request.query_params.get("name", None)
        queryset = MoneyGiver.objects.all()
        if debt_sum:
            queryset = queryset.filter(debt_sum=debt_sum)

        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MoneyGiverSerializer
        elif self.request.method == "POST":
            return MoneyGiverInputSerializer
        elif self.request.method == "PATCH":
            return MoneyGiverUpdateSerializer
        else:
            raise MethodNotAllowed(self.request.method)

    def patch(self, request, *args, **kwargs):
        initial_data = request.data #Переменная initial_data = всё что находится в body запроса
        serializer_class = self.get_serializer_class() #serializer = обращение к функции get_serializer_class, которая знает, что мы сделали запрос patch
        serializer = serializer_class(data=initial_data)
        serializer.is_valid(raise_exception=True) #Провалидировали body на предмет коректности. ВСЕ ПОЛЯ

        people = MoneyGiver.objects.get(pk=serializer.data["id"]) #objects общение с объектами данной модели
        people.phone_number = serializer.data["phone_number"]
        people.save()
        return Response(MoneyGiverSerializer(people).data)

