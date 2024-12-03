from rest_framework import viewsets
from api.serializers import PortifolioOwnerSerializer, ProjectSerializer, ServiceSerializer
from api.models import PortifolioOwner, Project, Service

class PortifolioOwnerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PortifolioOwnerSerializer

    def get_queryset(self):
        # Retorna apenas o último registro de PortifolioOwner
        last_owner = PortifolioOwner.objects.last()
        if last_owner:
            return PortifolioOwner.objects.filter(pk=last_owner.pk)
        return PortifolioOwner.objects.none()

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all().filter(is_published=True)
    serializer_class = ServiceSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().filter(is_published=True)
    serializer_class = ProjectSerializer
