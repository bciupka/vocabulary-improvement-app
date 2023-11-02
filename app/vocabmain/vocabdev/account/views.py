from .models import ImpUser
from .serializers import ImpUserRegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication


class ImpUserRegisterView(CreateAPIView):
    queryset = ImpUser.objects.all()
    serializer_class = ImpUserRegisterSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [SessionAuthentication]
