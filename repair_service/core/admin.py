from django.contrib import admin

# Register your models here

from django.contrib import admin
from .models import ServiceRequest

from django.contrib import admin
from .models import FAQ

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product_name', 'serial_number', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('user__username', 'product_name', 'serial_number', 'status')
    


admin.site.register(FAQ)    