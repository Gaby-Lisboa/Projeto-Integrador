from django.urls import path, include
from . import views
from app_smart.api.viewsets import CreateUserAPIViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app_smart.api.viewsets import CreateUserAPIViewSet, SensorViewSet, TemperaturaDataViewSet, UmidadeDataViewSet, LuminosidadeDataViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import upload_csv_view
from app_smart.api.filters import SensorFilterView, TemperaturaFilterView, UmidadeFilterView, LuminosidadeFilterView


router = DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'temperatura', TemperaturaDataViewSet)
router.register(r'umidade', UmidadeDataViewSet)
router.register(r'luminosidade', LuminosidadeDataViewSet)

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('api/create_user/', CreateUserAPIViewSet.as_view(), name='create_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('upload_csv/', upload_csv_view, name='upload_csv'),
    path('api/sensor_filter/', SensorFilterView.as_view(), name='sensor_filter'), # Nova rota para filtragem personalizada
    path('api/temperatura_filter/', TemperaturaFilterView.as_view(), name='temperatura_filter'),
    path('api/umidade_filter/', UmidadeFilterView.as_view(), name='umidade_filter'),
]

