from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ArticleCategoryModel(models.Model):
	category_name = models.CharField(max_length=255)
	category_slug = models.SlugField(max_length=255)

	def __unicode__(self):
		return u'%s | %s ' % (self.category_name, self.category_slug)

class ArticlePageModel(models.Model):
	is_live = models.BooleanField(default=True)
	title_tag = models.CharField(max_length=255, null=True, blank=True, default=None)
	category = models.ForeignKey(ArticleCategoryModel)
	descriptive_url = models.SlugField(max_length=255)
	meta_description = models.CharField(max_length=255, null=True, blank=True, default=None)
	meta_keywords = models.CharField(max_length=500, null=True, blank=True, default=None)
	meta_author = models.CharField(max_length=255, null=True, blank=True, default=None)
	article_image = models.ImageField(upload_to="blog/",null=True,blank=True)
	article_title = models.TextField(null=True, blank=True, default=None)
	article_subheader = models.TextField(null=True, blank=True, default=None)
	article_text = models.TextField(null=True, blank=True, default=None)
	created_datetime = models.DateTimeField(auto_now_add=True)
	publish_time = models.DateTimeField()
	author = models.ForeignKey(User)
	
	def __unicode__(self):
		return u'%s | %s | %s' % (self.article_title, self.publish_time, self.descriptive_url)	
	
	class Meta:
		ordering = ['-created_datetime']

class ArticlePageViewCount(models.Model):
	page = models.ForeignKey(ArticlePageModel)
	numberOfViews = models.IntegerField()
	
	def __unicode__(self):
		return self.page

	class Meta:
		ordering = ['-numberOfViews']


