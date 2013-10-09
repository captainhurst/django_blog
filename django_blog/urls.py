from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from sitemap import ArticleSitemap, CategorySitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'aef.views.home', name='home'),
    #url(r'^aef/', include('aef.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
    url(r'', include('landing_page.urls')),
	url(r'', include('contact.urls')),
	url(r'', include('articles.urls')),
	
)


sitemaps = {
    'article': ArticleSitemap,
	'category': CategorySitemap,
}

urlpatterns += patterns('',
    (r'^sitemap\.xml', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
