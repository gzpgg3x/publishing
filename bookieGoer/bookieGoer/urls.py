from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'discover.views.shout'),
    url(r'^shout$', 'discover.views.shout'),
    
    url(r'^api/shouts/new$', 'discover.api.new_shout'),
    url(r'^api/shouts/get$', 'discover.api.get_shouts'),
    
    url(r'^admin/', include(admin.site.urls)),
)
