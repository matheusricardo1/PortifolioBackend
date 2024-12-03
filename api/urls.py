from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'owner', views.PortifolioOwnerViewSet, basename='owner')
router.register(r'services', views.ServiceViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
