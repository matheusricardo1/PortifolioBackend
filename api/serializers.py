from rest_framework.serializers import ModelSerializer
from .models import PortifolioOwner, Project, Service


class PortifolioOwnerSerializer(ModelSerializer):
    class Meta:
        model = PortifolioOwner
        fields = '__all__'     
   
        
class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
