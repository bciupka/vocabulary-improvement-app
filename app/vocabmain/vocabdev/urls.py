from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from .improver import views


router = routers.DefaultRouter()
router.register(r'language', views.LanguageViewSet)
router.register(r'word', views.WordViewSet)
router.register(r'link', views.LinkViewSet)
# router.register(r'test', views.test_endpoint, basename='test_endpoint')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/eptest/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/testme', views.test_endpoint),
    path('api/', include(router.urls)),
    ]
