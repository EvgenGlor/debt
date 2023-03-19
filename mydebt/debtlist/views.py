from rest_framework.viewsets import ModelViewSet

from .models import Debt
from .serializers import DebtSerializer


class DebtView(ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

