from django.urls import path
from django.views.decorators.cache import never_cache

from . import views


urlpatterns = [
    path("", never_cache(views.BankView.as_view()), name="banks_list"),
]
