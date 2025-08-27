from rest_framework import serializers

from hospital import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__' # para criar uma lista tem que abrir colchetes

class TelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'

class HealthInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HealthInsurance
        fields = '__all__'

class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BloodType
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = '__all__'

class PatientHealthInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PatientHealthInsurance
        fields = '__all__'

class MedicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medic
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consultation
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medication
        fields = '__all__'

class MedicationConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicationConsultation
        fields = '__all__'

