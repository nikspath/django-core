from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
	title = models.CharField(max_length=20)

	class Meta:
		verbose_name="Category"
		verbose_name_plural="Category"
		ordering=['title']

	def __str__(self):
		return self.title	

class Post(models.Model):

	options=(
			('draft','Draft'),
			('published','Published')
		)

	category=models.ForeignKey(Category,on_delete=models.CASCADE,default='1')
	title=models.CharField(max_length=20, help_text="this is help text")
	slug=models.SlugField(max_length=200,unique_for_date='publish',null=True,blank=True)
	publish=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post',default='1')
	status=models.CharField(max_length=20,choices=options,default='draft')

	class Meta:
		verbose_name="Post"
		verbose_name_plural="Post"
		ordering=['-title']	

	def __str__(self):
		return self.title