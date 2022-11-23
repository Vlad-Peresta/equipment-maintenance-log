from django.db import models

from worker.models import Worker


class EquipmentType(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Equipment(models.Model):
    name = models.CharField(max_length=127, unique=True)
    inventory_number = models.CharField(max_length=63, unique=True)
    type = models.ForeignKey(
        EquipmentType,
        on_delete=models.CASCADE,
        related_name="equipment"
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "equipment"
        verbose_name_plural = "equipment"

    def __str__(self):
        return f"{self.name} - {self.type}"


class BreakdownType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Breakdown(models.Model):
    STATUS_CHOICES = (
        ("completed", "Completed"),
        ("process", "In process")
    )

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name="breakdowns"
    )
    repair_staff = models.ManyToManyField(Worker)
    breakdown_type = models.ForeignKey(
        BreakdownType,
        on_delete=models.CASCADE,
        related_name="breakdown_types"
    )
    circumstance = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="process"
    )
    repair_duration = models.DurationField(blank=True, null=True)

    class Meta:
        ordering = ["-time"]

    def __str__(self):
        return f"{self.equipment} - {self.time}"
