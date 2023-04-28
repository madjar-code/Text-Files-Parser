from django.contrib import admin
from .models import\
    ResumeData, PositionTime


# admin.site.register(ResumeData)
# admin.site.register(PositionTime)

@admin.register(PositionTime)
class PositionTimeAdmin(admin.ModelAdmin):
    model = PositionTime
    
    search_fields = (
        'position',
        'resume',
    )
    list_filter = (
        'resume',
    )
    list_display = (
        'id',
        'local_order',
        'position',
        'time',
        'resume',
    )


@admin.register(ResumeData)
class ResumeDataAdmin(admin.ModelAdmin):
    model = ResumeData
    
    search_fields = (
        'number',
        'link',
    )
    list_filter = (
        'link',
    )
    list_display = (
        'id',
        'number',
        'link',
    )
