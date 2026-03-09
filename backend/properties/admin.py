from django.contrib import admin
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'price_per_month', 'owner', 'is_available']
    search_fields = ['title', 'address', 'city']
    list_filter = ['property_type', 'is_available', 'created_at']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'property_type')
        }),
        ('Location', {
            'fields': ('address', 'city', 'country')
        }),
        ('Details', {
            'fields': ('bedrooms', 'bathrooms', 'square_feet')
        }),
        ('Pricing & Availability', {
            'fields': ('price_per_month', 'available_from', 'is_available')
        }),
        ('Images & Rating', {
            'fields': ('main_image', 'rating')
        }),
        ('Owner', {
            'fields': ('owner',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )