from .models import ImpUser
from .serializers import ImpUserRegisterSerializer
from rest_framework.generics import CreateAPIView


class ImpUserRegisterView(CreateAPIView):
    queryset = ImpUser.objects.all()
    serializer_class = ImpUserRegisterSerializer
