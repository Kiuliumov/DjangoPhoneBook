from rest_framework.routers import DefaultRouter

from .views import PhoneBookRecordViewSet

router = DefaultRouter()

router.register("records", PhoneBookRecordViewSet, basename="phonebook-records")

urlpatterns = router.urls
