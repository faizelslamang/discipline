from django.contrib import admin

# Register your models here.

from .models import Student, Incident, Interaction


class InteractionInline(admin.TabularInline):
    model = Interaction
    extra = 1


class IncidentInline(admin.TabularInline):
    model = Incident
    extra = 1


class IncidentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['student', ]
    inlines = [InteractionInline, ]
    search_fields = ['student__first_names', 'student__last_name',
                     'incident_type', ]
    list_filter = ['status', ]


class StudentAdmin(admin.ModelAdmin):
    inlines = [IncidentInline, ]
    search_fields = ['first_names', 'last_name', ]


admin.site.register(Student, StudentAdmin)
admin.site.register(Incident, IncidentAdmin)
# admin.site.register(Interaction)
