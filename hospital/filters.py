from django_filters import rest_framework as filters

from hospital import models

# Filtros de pesquisa
LIKE = 'unaccent__icontains' # Usando unaccent para ignorar acentos e trazer palavras semelhantes
ICONTAINS = 'icontains' # Usando icontains para trazer palavras semelhantes
UNACCENT_IEXACT = 'unaccent__iexact' # Usando unaccent para ignorar acentos e trazer palavras exatas
EQUALS = 'exact' # Usando exact para trazer o campo exatas
STARTS_WITH = 'startswith' # Usando startswith para trazer palavras que começam com o termo pesquisado
GT = 'gt' # maior que
LT = 'lt' # menor que
GTE = 'gte' # maior ou igual a
LTE = 'lte' # menor ou igual a
IN = 'in' # Usando in para trazer palavras que estão na lista

class UserFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    name = (filters.CharFilter(field_name='name', lookup_expr='icontains'))
    email = (filters.CharFilter(field_name='email', lookup_expr='icontains'))
    cpf = (filters.CharFilter(field_name='cpf', lookup_expr='icontains'))
    sex = (filters.ChoiceFilter(choices=models.User.sex_choices))

    class Meta:
        model = models.User
        fields = ['id','name','email','cpf','sex']

class TelephoneFilter(filters.FilterSet):
    number = (filters.CharFilter(field_name='number', lookup_expr='icontains'))
    user_id = (filters.NumberFilter(field_name='user_id'))

    class Meta:
        model = models.Telephone
        fields = ['number','user']

class AddressFilter(filters.FilterSet):
    postal_code = filters.CharFilter(lookup_expr='icontains')
    number_house = filters.CharFilter(lookup_expr='icontains')
    user_id = filters.NumberFilter(field_name='user__id')

    class Meta:
        model = models.Address
        fields = ['postal_code', 'number_house', 'user']

class HealthInsuranceFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.HealthInsurance
        fields = ['name']

class BloodTypeFilter(filters.FilterSet):
    name = filters.ChoiceFilter(choices=models.BloodType.type_choices)

    class Meta:
        model = models.BloodType
        fields = ['name']

class PatientFilter(filters.FilterSet):
    weight_min = filters.NumberFilter(field_name='weight', lookup_expr='gte')
    weight_max = filters.NumberFilter(field_name='weight', lookup_expr='lte')
    height_min = filters.NumberFilter(field_name='height', lookup_expr='gte')
    height_max = filters.NumberFilter(field_name='height', lookup_expr='lte')
    blood_type = filters.ModelChoiceFilter(queryset=models.BloodType.objects.all())
    user_id = filters.NumberFilter(field_name='user__id')

    class Meta:
        model = models.Patient
        fields = ['weight', 'height', 'blood_type', 'user']

class PatientHealthInsuranceFilter(filters.FilterSet):
    type = filters.ChoiceFilter(choices=models.PatientHealthInsurance.type_choice)
    waiting_period_after = filters.DateFilter(field_name='waiting_period', lookup_expr='gte')
    waiting_period_before = filters.DateFilter(field_name='waiting_period', lookup_expr='lte')
    health_insurance = filters.ModelChoiceFilter(queryset=models.HealthInsurance.objects.all())
    patient = filters.ModelChoiceFilter(queryset=models.Patient.objects.all())

    class Meta:
        model = models.PatientHealthInsurance
        fields = ['type', 'health_insurance', 'patient']

class MedicFilter(filters.FilterSet):
    crm = filters.CharFilter(lookup_expr='icontains')
    user_id = filters.NumberFilter(field_name='user__id')
    specialization = filters.ModelMultipleChoiceFilter(
        queryset=models.Specialization.objects.all(),
        field_name='specialization__id',
        to_field_name='id'
    )

    class Meta:
        model = models.Medic
        fields = ['crm', 'user', 'specialization']

class SpecializationFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Specialization
        fields = ['name']

class ConsultationFilter(filters.FilterSet):
    date_after = filters.DateTimeFilter(field_name='time_consultation', lookup_expr='gte')
    date_before = filters.DateTimeFilter(field_name='time_consultation', lookup_expr='lte')
    medic_attended = filters.BooleanFilter()
    patient_attended = filters.BooleanFilter()
    medic = filters.ModelChoiceFilter(queryset=models.Medic.objects.all())
    patient = filters.ModelChoiceFilter(queryset=models.Patient.objects.all())

    class Meta:
        model = models.Consultation
        fields = ['time_consultation', 'diagnosis', 'medic_attended','patient_attended', 'medic', 'patient']

class MedicationFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    type_application = filters.ChoiceFilter(choices=models.Medication.application_choice)
    type_dosage = filters.ChoiceFilter(choices=models.Medication.dosage_choice)

    class Meta:
        model = models.Medication
        fields = ['name', 'type_application', 'type_dosage']

class MedicationConsultationFilter(filters.FilterSet):
    dosage_min = filters.NumberFilter(field_name='dosage', lookup_expr='gte')
    dosage_max = filters.NumberFilter(field_name='dosage', lookup_expr='lte')
    consultation = filters.ModelChoiceFilter(queryset=models.Consultation.objects.all())
    medication = filters.ModelChoiceFilter(queryset=models.Medication.objects.all())

    class Meta:
        model = models.MedicationConsultation
        fields = ['dosage', 'consultation', 'medication']