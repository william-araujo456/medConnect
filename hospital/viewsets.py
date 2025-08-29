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


class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    filterset_class = filters.PatientFilter
    permission_classes = [IsAuthenticated]


class MedicViewSet(viewsets.ModelViewSet):
    queryset = models.Medic.objects.all()
    serializer_class = serializers.MedicSerializer
    filterset_class = filters.MedicFilter
    permission_classes = [IsAuthenticated]


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    filterset_class = filters.SpecializationFilter
    permission_classes = [IsAuthenticated]


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = models.Consultation.objects.all()
    serializer_class = serializers.ConsultationSerializer
    filterset_class = filters.ConsultationFilter
    permission_classes = [IsAuthenticated]


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = models.Medication.objects.all()
    serializer_class = serializers.MedicationSerializer
    filterset_class = filters.MedicationFilter
    permission_classes = [IsAuthenticated]


class MedicationConsultationViewSet(viewsets.ModelViewSet):
    queryset = models.MedicationConsultation.objects.all()
    serializer_class = serializers.MedicationConsultationSerializer
    filterset_class = filters.MedicationConsultationFilter
    permission_classes = [IsAuthenticated]
