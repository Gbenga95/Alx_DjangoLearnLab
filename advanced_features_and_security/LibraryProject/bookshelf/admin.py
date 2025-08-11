from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')

    # Fields to filter by in the right sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # Fieldsets for viewing/editing a user
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Fieldsets for creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
