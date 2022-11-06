from django.contrib import admin
from .models import review, Patient

# Register your models here.
admin.site.register(review)
admin.site.register(Patient)