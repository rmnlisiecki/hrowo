from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Samochody2.views',
    # Examples:
    url(r'^$', 'hotel', name='hotel'),
    url(r'^index$', 'index', name='index'),
    url(r'^hotel$', 'hotel', name='hotel'),
    url(r'^hotel_selected\d$', 'hotel_selected', name='hotel_selected'),
    url(r'^table_activities$', 'table_activities', name='table_activities'),
    url(r'^food$', 'food', name='food'),
    url(r'^interior_design$', 'interior_design', name='interior_design'),
    url(r'^costs$', 'costs', name='costs'),
    url(r'^location_map$', 'location_map', name='location_map'),
    url(r'^contact$', 'contact', name='contact'),
    url(r'^social_media$', 'social_media', name='social_media'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
