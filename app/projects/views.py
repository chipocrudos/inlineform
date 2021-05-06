from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404
from .models import Contract, Task, PaymentCondition
from .forms import ContractForm, TaskFormSet, PaymentConditionForm


class ConstractListView(ListView):
    model = Contract

    def get_queryset(self):
        queryset = super(ConstractListView, self).get_queryset()

        return queryset.annotate(
            taskcomplete=Count("task__id"),
            paymentcomplete=Count("paymentcondition__id"),
        )


class ContractDetailView(DetailView):
    model = Contract
    slug_field = "code"


class ConstractCreateView(CreateView):
    model = Contract
    form_class = ContractForm

    def get_success_url(self):

        return reverse_lazy("project:newtasks", args=(self.object,))


class PaymentConditionCreateView(CreateView):
    model = PaymentCondition
    form_class = PaymentConditionForm
    success_url = reverse_lazy("project:contractlist")

    def get_context_data(self, **kwargs):
        context = super(PaymentConditionCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["task_form"] = TaskFormSet(self.request.POST)
        else:
            context["task_form"] = TaskFormSet()
        return context

    def get_initial(self):
        initial = super(PaymentConditionCreateView, self).get_initial()

        initial = initial.copy()
        self.contract = get_object_or_404(Contract, code=self.kwargs.get("code"))
        initial["contract"] = self.contract

        return initial

    def form_invalid(self, form):
        context = self.get_context_data()
        task_form = context["task_form"]
        task_form.is_valid()
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        context = self.get_context_data()
        self.obj = form.save()
        task_form = context["task_form"]
        if task_form.is_valid():
            # task_form.instance = self.bj
            task_form.instance = self.contract
            task_form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
