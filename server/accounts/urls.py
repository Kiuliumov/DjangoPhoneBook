from rest_framework.routers import DefaultRouter

from .views import AccountViewSet, UserViewSet

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("accounts", AccountViewSet, basename="accounts")

urlpatterns = router.urls
