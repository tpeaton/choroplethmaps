from django.conf.urls import patterns, include, url
from django.contrib import admin

from maps.views import ViewHome, ViewMaps

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^maps/', ViewMaps.as_view(), name='maps'),
    url(r'^', ViewHome.as_view(), name='home'),
)
