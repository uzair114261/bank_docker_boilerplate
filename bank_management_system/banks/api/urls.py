from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

urlpatterns = [
    path("list/generic", views.BankListGenericView.as_view(), name="bank_list"),
    path(
        "actions/generic/<int:id>",
        views.BankActionGenericView.as_view(),
        name="bank_generic_action",
    ),
    path("apiview", views.BankAPIView.as_view(), name="bank_apiview"),
]

router.register(r"list/viewset", views.BankViewSet, basename="bank_list_viewset")
urlpatterns += router.urls
