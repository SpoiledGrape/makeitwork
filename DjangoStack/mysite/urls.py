from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^requests/", include("requests.urls")),
    url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    #used for notifications
    url(r"^notifications/", include("pinax.notifications.urls"))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
