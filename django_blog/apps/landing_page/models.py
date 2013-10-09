from django.db import models

# Create your models here.
#from articles.models import ArticlePageModel, ArticleCategoryModel, ArticlePageViewCount


class LandingPageModel(models.Model):
	titleTag = models.CharField(max_length=255, null=True, blank=True, default=None)
	
	def __unicode__(self):
		return u'%s' % (self.titleTag)	

class LandingPageMeta(models.Model):
	metaDescription = models.CharField(max_length=255, null=True, blank=True, default=None)
	metaKeywords = models.CharField(max_length=500, null=True, blank=True, default=None)
	metaAuthor = models.CharField(max_length=255, null=True, blank=True, default=None)
	
	def __unicode__(self):
		return u'%s | %s' % (self.metaDescription, self.metaKeywords)

class EmailCaptureModel(models.Model):
	email = models.EmailField(max_length=255)
	capture_date = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return u'%s | %s' % (self.email, self.capture_date)
	
class LandingImageContentModel(models.Model):
	rank = models.IntegerField(max_length=1)
	landing_image = models.ImageField(upload_to='/landing/main',null=True,blank=True)
	title = models.CharField(max_length=500, null=True, blank=True, default=None)
	content = models.TextField( null=True, blank=True, default=None)
	created_datetime = models.DateTimeField()

	def __unicode__(self):
		return u'%s | %s | %s ' % (self.title, self.rank, self.created_datetime)

	class Meta:
		ordering = ['rank']

class LandingContent(models.Model):
	rank = models.IntegerField(max_length=1)
	landing_content_image = models.ImageField(upload_to='/blog/content',null=True,blank=True)
	title = models.CharField(max_length=255, null=True, blank=True, default=True)
	seo_content = models.TextField(null=True, blank=True, default=None)
	
	class Meta:
		ordering = ['rank']


