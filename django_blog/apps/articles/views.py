# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.contrib import auth
from django.conf import settings as conf_settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.sites.models import Site
from django.contrib.sites.models import get_current_site
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import IntegrityError
from urlparse import urlparse
from datetime import datetime
import simplejson
import string

from models import ArticlePageModel, ArticleCategoryModel, ArticlePageViewCount
from landing_page_aef.forms import EmailCaptureForm


def about_page(request):
	#page = ArticlePageModel.objects.get(descriptive_url='about')
	#featured = ArticleCategoryModel.objects.all()
	ecForm = EmailCaptureForm()
	
	#fd = []
	#for f in featured:
	#	fd += ArticlePageModel.objects.filter(id=f.id).order_by('-created_datetime')
	context = {'ecForm': ecForm}
	return render(request, 'about.html', context)
	
def article_main(request):
	ecForm = EmailCaptureForm()
	featured = ArticleCategoryModel.objects.all().order_by('category_name')
	for f in featured:
		f.page = ArticlePageModel.objects.filter(category=f).filter(is_live=True).order_by('-created_datetime').exclude(publish_time__gt=datetime.now())[:5]
	context = {'featured': featured, 'ecForm': ecForm}
	return render(request, 'articles_directory.html', context)

def article_category_main(request, category):
	ecForm = EmailCaptureForm()
	
	featured = ArticleCategoryModel.objects.get(category_slug=category)
	page = ArticlePageModel.objects.filter(category=featured).order_by('-created_datetime')
	context = {'page': page, 'ecForm': ecForm, 'categoryHeader': featured }
	return render(request, 'articles_directory.html', context)	
	
def article(request, category,  article_slug):
	page = ArticlePageModel.objects.get(descriptive_url=article_slug)
	ecForm = EmailCaptureForm()
	
	featured = ArticleCategoryModel.objects.filter(category_slug=category)
	
	fd = ArticlePageModel.objects.filter(category=featured).order_by('-created_datetime')
	context = {'page': page, 'featured': fd, 'ecForm': ecForm}
	return render(request, 'articles.html', context)
	

