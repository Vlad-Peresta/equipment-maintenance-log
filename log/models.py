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
    repair_duration = models.DurationField(blank=True)

    class Meta:
        ordering = ["-time"]

    def __str__(self):
        return f"{self.equipment} - {self.time}"


class TaskType(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("urgent", "Urgent"),
        ("high", "High"),
        ("low", "Low")
    )

    name = models.CharField(max_length=127)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    assignees = models.ManyToManyField(Worker)

    class Meta:
        ordering = ["is_completed", "deadline"]

    def __str__(self):
        return f"{self.name}, is_completed - {self.is_completed}"
