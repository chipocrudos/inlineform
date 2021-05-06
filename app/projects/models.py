from django.db import models
import uuid


class Contract(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=180)

    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"

    def __str__(self):
        return f"{self.code}"


class Task(models.Model):

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{self.title}"


class PaymentCondition(models.Model):
    CONDITION1 = 1
    CONDITION2 = 2
    CONDITION3 = 3

    CONDITION_CHOICES = (
        (CONDITION1, "CONDITION1"),
        (CONDITION2, "CONDITION2"),
        (CONDITION3, "CONDITION3"),
    )

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    condition = models.PositiveSmallIntegerField(choices=CONDITION_CHOICES)

    class Meta:
        verbose_name = "PaymentCondition"
        verbose_name_plural = "PaymentConditions"

    def __str__(self):
        return f"{self.condition}"
