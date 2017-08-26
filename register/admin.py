from django.contrib import admin

from .models import Team, Contestant

@admin.register(Contestant)
class ContestantAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email', 'team']

    list_display = ('first_name', 'last_name', 'email', 'team')
    list_display_links = ('first_name', 'last_name', 'email')

    readonly_fields = ('team',)

    fieldsets = [
        ('Name', {'fields': ['first_name', 'last_name']}),
        ('Personal Information', {'fields': ['email', 'team']}),
    ]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name', 'school']

    class ContestantInline(admin.TabularInline):
        model = Contestant
        extra = 2

    list_display = ('name', 'school')
    list_display_links = ('name',)

    fieldsets = [
        ('Information', {'fields': ['name', 'school']}),
    ]

    inlines = [ContestantInline]