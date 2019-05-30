from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from core.views import ping
from trood_reporting.views import ReportViewSet, SourceViewSet


schema_view = get_schema_view(
    openapi.Info(
        title='Trood BI Reporting API',
        default_version='v1',
        contact=openapi.Contact(email="info@trood.ru"),
        license=openapi.License(name="Private License"),
    ),
    url=settings.API_URL,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'reports', ReportViewSet)
router.register(r'connections', SourceViewSet)

urlpatterns = [

    url(r'^ping/$', ping, name='ping'),

    url(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema'
    ),

    url(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-ui'
    ),

    url(r'^v1/', include((router.urls, 'v1'), namespace='v1')),

    url(r'^reporting/admin/', admin.site.urls),
]

# Debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
