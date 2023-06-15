from django.contrib import admin
from .models import Post,Category
from django.apps import apps
from django.contrib.sessions.models import Session
from django import forms
from .models import Post
 
# Register your models here.

class PostForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(PostForm,self).__init__(*args,**kwargs)
		self.fields['title'].help_text = 'this is admin title'

	class Meta:
		model = Post
		exclude = ('',)

class PostAdmin(admin.ModelAdmin):
	form = PostForm

admin.site.register(Post,PostAdmin)					


# models = apps.get_models()
# print(models)
# for model in models:
# 	try:
# 		admin.site.register(model)
# 	except admin.sites.AlreadyRegistered:
# 		pass	

# admin.site.unregister(Session)		
# admin.site.register(Post)
# admin.site.register(Category)