from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import PortifolioOwnerSerializer, PortifolioOwnerAboutSerializer, ProjectSerializer, ServiceSerializer
from .models import PortifolioOwner, Project, Service


class GetPortifolioOwner(APIView):
    def get(self, request, format=None):       
        portifolio_owner = PortifolioOwner.objects.last()
        serializer = PortifolioOwnerSerializer(portifolio_owner)
        return Response(serializer.data, status=200)
         
class GetPortifolioOwnerAbout(APIView):
    def get(self, request, format=None):       
        portifolio_owner = PortifolioOwner.objects.all().first()
        serializer = PortifolioOwnerAboutSerializer(portifolio_owner)
        return Response(serializer.data)
    
class GetServices(APIView):
    def get(self, request, format=None):       
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class GetProjects(APIView):
    def get(self, request, format=None):       
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
