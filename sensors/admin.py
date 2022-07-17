from django.contrib.admin import AdminSite
from rest_framework.reverse import reverse_lazy


class SensorsAdminSite(AdminSite):
    site_header = "Sensor management admin site"
    site_title = "Sensors"
    site_url = reverse_lazy("continuoussensor-list")
