from django.conf.urls import patterns, include, url
from django.contrib import admin

from testapp.views import SomethingCreate

urlpatterns = patterns('',
    url(r'^create/', SomethingCreate.as_view(), name='create'),
    url(r'^admin/', include(admin.site.urls)),
)
