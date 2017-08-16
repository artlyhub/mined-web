from django.contrib.auth.models import User
from keyst_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .models import KeystData
from .serializers import KeystDataSerializer


class KeystDataView(generics.ListCreateAPIView):
    queryset = KeystData.objects.all()
    serializer_class = KeystDataSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)


class KeystDataDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KeystData.objects.all()
    serializer_class = KeystDataSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly)
