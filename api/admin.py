from django.contrib import admin
from .models import PortifolioOwner, Project, Service
from adminsortable2.admin import SortableAdminMixin


admin.site.register(PortifolioOwner)
admin.site.register(Service)
admin.site.register(Project)