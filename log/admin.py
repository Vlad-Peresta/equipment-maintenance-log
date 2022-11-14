from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from log.models import (
    Position,
    EquipmentType,
    BreakdownType,
    TaskType,
    Equipment,
    Breakdown,
    Task,
    Worker,
)


admin.site.register(Position)
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


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info", {"fields": ("position",)}
        ),

    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": ("position",)
            }
        ),
    )
