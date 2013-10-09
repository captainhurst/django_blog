from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
import datetime
from random import randrange
from articles.models import ArticleCategoryModel, ArticlePageModel

class ArticleSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.7
	
	def items(self):
		return ArticlePageModel.objects.all()
	
	def lastmod(self, obj):
		return obj.created_datetime
	
	def location(self, obj):
		return '/blog/%s/%s/' % (obj.category.category_slug, obj.descriptive_url)

class CategorySitemap(Sitemap):
	changefreq = "daily"
	priority = 0.7
	
	def items(self):
		return ArticleCategoryModel.objects.all()
	
	def lastmod(self, obj):
		return datetime.datetime.now()

	def location(self, obj):
		return "/blog/%s/" % obj.category_slug
