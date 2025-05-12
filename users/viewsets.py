from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from .permissions import IsUserOwnerGetAndPostOnly

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer