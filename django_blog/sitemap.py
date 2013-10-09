from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
import datetime
from random import randrange
from news_aef.models import NewsArticleModel
from articles_aef.models import ArticleCategoryModel, ArticlePageModel
from projects_aef.models import ProjectModel

class ArticleSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.7
	
	def items(self):
		return ArticlePageModel.objects.all()
	
	def lastmod(self, obj):
		return obj.created_datetime
	
	def location(self, obj):
		return '/blog/%s/%s/' % (obj.category.category_slug, obj.descriptive_url)
		
class NewsSitemap(Sitemap):
	changefreq = "daily"
	priority = 0.7

	def items(self):
		return NewsArticleModel.objects.all()

	def lastmod(self, obj):
		return obj.created_datetime

	def location(self, obj):
		return '/news/%s/' % obj.descriptive_url

class CategorySitemap(Sitemap):
	changefreq = "daily"
	priority = 0.7
	
	def items(self):
		return ArticleCategoryModel.objects.all()
	
	def lastmod(self, obj):
		return datetime.datetime.now()

	def location(self, obj):
		return "/blog/%s/" % obj.category_slug

class ProjectsSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.9
	
	def items(self):
		return ProjectModel.objects.all()
	
	def lastmod(self, obj):
		return datetime.datetime.now()
	
	def location(self, obj):
		locs = ProjectModel.objects.all()
		
		return '/projects/%s' % (obj.descriptive_url)