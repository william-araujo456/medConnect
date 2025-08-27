# É onde vamos colocar a rota dos endereços de endpoint.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from hospital import models, serializers, filters

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_class = filters.UserFilter
    permission_classes = [IsAuthenticated]

class TelephoneViewSet(viewsets.ModelViewSet):
    queryset = models.Telephone.objects.all()
    serializer_class = serializers.TelephoneSerializer
    filterset_class = filters.TelephoneFilter
    permission_classes = [IsAuthenticated]

class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    filterset_class = filters.AddressFilter
    permission_classes = [IsAuthenticated]

class HealthInsuranceViewSet(viewsets.ModelViewSet):
    queryset = models.HealthInsurance.objects.all()
    serializer_class = serializers.HealthInsuranceSerializer
    filterset_class = filters.HealthInsuranceFilter
    permission_classes = [IsAuthenticated]

class BloodTypeViewSet(viewsets.ModelViewSet):
    queryset = models.BloodType.objects.all()
    serializer_class = serializers.BloodTypeSerializer
    filterset_class = filters.BloodTypeFilter
    permission_classes = [IsAuthenticated]