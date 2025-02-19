from django.urls import path
from django.views.decorators.cache import never_cache

from . import views


urlpatterns = [
    path("", never_cache(views.AccountView.as_view()), name="account_list"),
]
