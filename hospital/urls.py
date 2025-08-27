from rest_framework import routers

from hospital import viewsets

router = routers.DefaultRouter()

router.register('users', viewsets.UserViewSet)
router.register('telephones', viewsets.TelephoneViewSet)
router.register('addresses', viewsets.AddressViewSet)
router.register('bloodtypes', viewsets.BloodTypeViewSet)

urlpatterns = router.urls
