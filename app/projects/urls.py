from django.urls import path
from .views import (
    ConstractListView,
    ContractDetailView,
    ConstractCreateView,
    PaymentConditionCreateView,
)

app_name = "project"

# contracts path
urlpatterns = [
    path("", ConstractListView.as_view(), name="contractlist"),
    path("contract/", ConstractCreateView.as_view(), name="newcontract"),
    path("contract/<uuid:slug>/", ContractDetailView.as_view(), name="contract"),
]

# task form inline + payment
urlpatterns += [
    path(
        "contract/<uuid:code>/tasks/",
        PaymentConditionCreateView.as_view(),
        name="newtasks",
    )
]
