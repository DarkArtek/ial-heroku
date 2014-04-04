from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'herokutest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'onepage.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
