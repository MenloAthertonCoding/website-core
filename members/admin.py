from django.contrib import admin

from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email', 'website']

    list_display = ('first_name', 'last_name', 'email')
    list_display_links = ('first_name', 'last_name', 'email')

    fieldsets = [
        ('Name', {'fields': ['first_name', 'last_name']}),
        ('Personal Information', {'fields': ['email', 'profile_image', 'website']}),
    ]