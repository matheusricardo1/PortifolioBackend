from django.contrib import admin
from .models import PortifolioOwner, Project, Service


admin.site.register(PortifolioOwner)
admin.site.register(Service)
admin.site.register(Project)
