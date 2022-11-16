from django.contrib import admin

from log.models import (
    EquipmentType,
    BreakdownType,
    TaskType,
    Equipment,
    Breakdown,
    Task,
)


admin.site.register(EquipmentType)
admin.site.register(BreakdownType)
admin.site.register(TaskType)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "inventory_number", "type")
    search_fields = ("name",)
    list_filter = ("type",)


@admin.register(Breakdown)
class BreakdownAdmin(admin.ModelAdmin):
    list_display = (
        "equipment", "breakdown_type", "time", "repair_duration", "status",)
    search_fields = ("equipment", "breakdown_type",)
    list_filter = ("equipment", "repair_staff", "breakdown_type", "time",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "is_completed", "task_type",)
    search_fields = ("name",)


