from django.conf.urls import patterns, include, url
from articles.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('articles.views',
	#url(r'^$', landing),
	#url(r'^about/$', about_page),
	url(r'^articles/$', article_main),
	url(r'^articles/(?P<category>[a-z-0-9]+)/$', article_category_main),
	url(r'^articles/(?P<category>[a-z-0-9]+)/(?P<article_slug>[a-z-0-9]+)/$', article),
	
	#url(r'^login/$', user_login),
	#url(r'^logout/$', logout),

	
	#url(r'^register/$', register),
	#url(r'^forgot_password/$', forgot_password),
	#url(r'^settings/$', settings),
	

	# Examples:
	# url(r'^$', 'mylifing.views.home', name='home'),
	# url(r'^mylifing/', include('mylifing.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# url(r'^admin/', include(admin.site.urls)),
)
