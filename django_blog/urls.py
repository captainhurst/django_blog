from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from sitemap import ArticleSitemap, NewsSitemap, CategorySitemap, ProjectsSitemap

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
    url(r'', include('landing_page_aef.urls')),
	url(r'', include('contact_aef.urls')),
	url(r'', include('articles_aef.urls')),
	
)


sitemaps = {
    'article': ArticleSitemap,
	'category': CategorySitemap,
	'news': NewsSitemap,
	'projects': ProjectsSitemap,
}

urlpatterns += patterns('',
    (r'^sitemap\.xml', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
