from django import forms
from django.forms.models import inlineformset_factory
from .models import Contract, Task, PaymentCondition


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class PaymentConditionForm(forms.ModelForm):
    class Meta:
        model = PaymentCondition
        fields = "__all__"

        widgets = {"contract": forms.HiddenInput()}


TaskFormSet = inlineformset_factory(
    Contract, Task, form=TaskForm, can_delete=False, extra=5
)
