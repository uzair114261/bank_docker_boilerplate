from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


schema_view = get_schema_view(
    openapi.Info(
        title="bank_management_system API",
        default_version="v1",
    ),
    public=True,
    url=settings.API_BASE_URL,
    permission_classes=(IsAuthenticated,),
    authentication_classes=(BasicAuthentication,),
)

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path("admin/", admin.site.urls),
    path("banks/", include("bank_management_system.banks.urls")),
    path("accounts/", include("bank_management_system.accounts.urls")),
    path("authentication/", include("bank_management_system.authentication.urls")),
    # Base routes for APIs
    path("api/banks/", include("bank_management_system.banks.api.urls")),
    path("api/authentication/", include("bank_management_system.authentication.api.urls")),
    path("api/accounts/", include("bank_management_system.accounts.api.urls")),
]

if settings.ENABLE_DEBUG_TOOLS:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        path("silk/", include("silk.urls", namespace="silk")),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)