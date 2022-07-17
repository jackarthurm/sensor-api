from django.contrib.admin.apps import AdminConfig


class SensorsAdminConfig(AdminConfig):
    default_site = 'sensors.admin.SensorsAdminSite'
