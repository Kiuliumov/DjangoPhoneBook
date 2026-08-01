from rest_framework import permissions, viewsets

from .models import PhoneBookRecord
from .serializers import PhoneBookRecordSerializer


class PhoneBookRecordViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneBookRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PhoneBookRecord.objects.filter(user=self.request.user)
