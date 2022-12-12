from django import forms

from task.models import TaskType


class TaskTypeForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Task type name",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = TaskType
        fields = ("name",)
