from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        db_column='created_at',
        auto_now_add=True,
        null=False
    )
    modified_at = models.DateTimeField(
        db_column='modified_at',
        auto_now=True,
        null=False
    )
    active = models.BooleanField(
        db_column='active',
        default=True,
        null=False
    )

    class Meta:
        abstract = True
        managed = True


class User(models.Model):
    class Sex(models.TextChoices):
        NOT_DEFINED = 'ND', 'Não definido'
        MALE = 'M', 'Masculino'
        FEMALE = 'F', 'Femenino'

    name = models.CharField(
        db_column='tx_name',
        max_length=255,
        null=False,
        blank=False
    )
    date_birth = models.DateField(
        db_column='dt_date_birth',
        null=False,
        blank=False
    )
    email = models.EmailField(
        db_column='tx_email',
        null=False,
        blank=False,
        unique=True
    )
    sex = models.CharField(
        db_column='cs_sex',
        max_length=10,
        null=False,
        blank=False,
        choices=Sex.choices,
        default=0
    )
    cpf = models.CharField(
        db_column='tx_cpf',
        max_length=11,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return f'{self.name} - {self.cpf}'

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Telephone(ModelBase):
    number = models.CharField(
        db_column='tx_number',
        max_length=11,
        null=False,
        unique=True
    )
    user = models.ForeignKey(
        User,
        db_column='id_user',
        on_delete=models.CASCADE,
        null=False
    )

    def __str__(self):
        return f'{self.id} - {self.number} - {self.user.name}'

    class Meta:
        db_table = 'telephone'
        verbose_name = 'Telephone'
        verbose_name_plural = 'Telephones'


class Address(ModelBase):
    postal_code = models.CharField(
        db_column='tx_postal_code',
        max_length=8,
        null=False,
        blank=False
    )
    number_house = models.CharField(
        db_column='tx_number_house',
        max_length=10,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        db_column='id_user',
        on_delete=models.CASCADE,
        null=False
    )

    def __str__(self):
        return f'{self.postal_code} - {self.number_house} - {self.user.name}'

    class Meta:
        db_table = 'address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class HealthInsurance(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=120,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        db_table = 'health_insurance'
        verbose_name = 'Health Insurance'
        verbose_name_plural = 'Health Insurances'


class Patient(ModelBase):
    class BloodType(models.TextChoices):
        AP = 'A+', 'A+'
        AN = 'A-', 'A-'
        BP = 'B+', 'B+'
        BN = 'B-', 'B-'
        ABP = 'AB+', 'AB+'
        ABN = 'AB-', 'AB-'
        OP = 'O+', 'O+'
        ON = 'O-', 'O-'

    user = models.ForeignKey(
        User,
        db_column='id_user',
        on_delete=models.CASCADE,
        null=False
    )
    weight = models.DecimalField(
        db_column='nb_weight',
        decimal_places=2,
        max_digits=5,
        null=False,
        blank=False
    )
    height = models.IntegerField(
        db_column='nb_height',
        null=False,
        blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(300)],
    )
    blood_type = models.CharField(
        db_column='cs_blood_type',
        max_length=5,
        null=False,
        blank=False,
        choices=BloodType.choices,
        default=BloodType.ABP
    )

    def __str__(self):
        return f'{self.id} - {self.user.name}'

    class Meta:
        db_table = 'patient'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class PatientHealthInsurance(ModelBase):
    class Type(models.IntegerChoices):
        NURSERY = 1, 'Enfermaria'
        APARTMENT = 2, 'Apartamento'

    insurance_number = models.CharField(
        db_column='tx_insurance_number',
        max_length=120,
        null=False,
        blank=False
    )

    ##choice
    type = models.CharField(
        db_column='cs_type',
        max_length=255,
        null=False,
        blank=False,
        choices=Type.choices,
        default=Type.NURSERY
    )
    waiting_period = models.DateField(
        db_column='dt_waiting_period',
        null=False,
        blank=False
    )
    health_insurance = models.ForeignKey(
        HealthInsurance,
        db_column='id_health_insurance',
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )
    patient = models.ForeignKey(
        Patient,
        db_column='id_patient',
        on_delete=models.CASCADE,
        null=False,
    )

    def __str__(self):
        return f'{self.type}'

    class Meta:
        db_table = 'patient_health_insurance'
        verbose_name = 'Patient Health Insurance'
        verbose_name_plural = 'Patients Health Insurances'


class Medic(ModelBase):
    crm = models.CharField(
        db_column='tx_crm',
        max_length=120,
        null=False,
        blank=False,
        unique=True,
    )
    user = models.ForeignKey(
        User,
        db_column='id_user',
        on_delete=models.CASCADE,
        null=False
    )

    specialization = models.ManyToManyField(
        'Specialization',
        db_table='specialization_medic',
    )

    def __str__(self):
        return f'{self.id} - {self.crm} - {self.user_id}'

    class Meta:
        db_table = 'medic'
        verbose_name = 'Medic'
        verbose_name_plural = 'Medics'


class Specialization(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=210,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'specialization'
        verbose_name = 'Specialization'
        verbose_name_plural = 'Specializations'


class Consultation(ModelBase):
    time_consultation = models.DateTimeField(
        db_column='dt_time_consultation',
        null=False,
        blank=False
    )
    diagnosis = models.TextField(
        db_column='tx_diagnosis',
        max_length=255,
        null=False,
        blank=False
    )
    medic_attended = models.BooleanField(
        db_column='cs_medic_attended',
        null=False,
        blank=False
    )
    patient_attended = models.BooleanField(
        db_column='cs_patient_attended',
        null=False,
        blank=False
    )
    patient = models.ForeignKey(
        Patient,
        db_column='id_patient',
        on_delete=models.PROTECT,
        null=False
    )
    medic = models.ForeignKey(
        Medic,
        db_column='id_medic',
        on_delete=models.PROTECT,
        null=False
    )

    medication = models.ManyToManyField(
        'Medication',
        through='MedicationConsultation'
    )

    def __str__(self):
        return f'{self.patient_id} - {self.medic_id}'

    class Meta:
        db_table = 'consultation'
        verbose_name = 'Consultation'
        verbose_name_plural = 'Consultations'


class Medication(ModelBase):
    class Application(models.IntegerChoices):
        ORAL = 1, 'Oral'
        INJECTABLE = 2, 'Injetável'

    class DosageType(models.IntegerChoices):
        ML = 1, 'ml'
        MG = 2, 'mg'

    name = models.CharField(
        db_column='tx_name',
        max_length=255,
        null=False,
    )
    # choices
    type_application = models.IntegerField(
        db_column='cs_type_application',
        null=False,
        choices=Application.choices
    )
    # choices
    type_dosage = models.CharField(
        db_column='cs_type_dosage',
        max_length=40,
        null=False,
        choices=DosageType.choices,
    )

    def __str__(self):
        return f'{self.name} - {self.type_application} - {self.type_dosage}'

    class Meta:
        db_table = 'medication'
        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'


class MedicationConsultation(ModelBase):
    medication = models.ForeignKey(
        Medication,
        db_column='id_medication',
        on_delete=models.PROTECT
    )
    consultation = models.ForeignKey(
        Consultation,
        db_column='id_consultation',
        on_delete=models.CASCADE
    )
    dosage = models.IntegerField(
        db_column='nb_dosage',
        null=False
    )

    def __str__(self):
        return f'{self.id} - {self.medication}'

    class Meta:
        db_table = 'medication_consultation'
        verbose_name = 'Medication Consultation'
        verbose_name_plural = 'Medication Consultations'
