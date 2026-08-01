from django.contrib.auth import get_user_model
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import Account

from .serializers import AccountSerializer, LoginSerializer, RegisterSerializer

User = get_user_model()


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ["register", "login"]:
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]

    @action(detail=False, methods=["post"])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response(
            {
                "id": user.id,
                "username": user.username,
            },
            status=status.HTTP_201_CREATED,
        )

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data)


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)
