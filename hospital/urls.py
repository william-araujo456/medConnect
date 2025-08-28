from rest_framework import routers

from hospital import viewsets

router = routers.DefaultRouter()

router.register('users', viewsets.UserViewSet)
router.register('telephones', viewsets.TelephoneViewSet)
router.register('addresses', viewsets.AddressViewSet)
router.register('health_insurances', viewsets.HealthInsuranceViewSet)
router.register('blood_types', viewsets.BloodTypeViewSet)
router.register('patients', viewsets.PatientViewSet)
router.register('medics', viewsets.MedicViewSet)
router.register('specializations', viewsets.SpecializationViewSet)
router.register('consultations', viewsets.ConsultationViewSet)
router.register('medications', viewsets.MedicationViewSet)
router.register('medication_consultations', viewsets.MedicationConsultationViewSet)

urlpatterns = router.urls
