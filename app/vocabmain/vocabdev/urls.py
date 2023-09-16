from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .improver import views


router = routers.DefaultRouter()
router.register(r'vocabuser', views.VocabUserViewset)
router.register(r'polish', views.PolishViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    ]
