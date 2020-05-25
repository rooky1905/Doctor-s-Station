from django.contrib import admin
from accounts.models import Patient,Doctor

#registering both models to display on admin site.
admin.site.register(Patient)
admin.site.register(Doctor)
