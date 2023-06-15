from django.contrib import admin
from post.models import Post

# Register your models here.
class CustomadminAdminArea(admin.AdminSite):
	site_header = 'Client Admin Site'
	site_title = 'Admin Site title'
	index_site	= 'Admin title'

TEXT = "some informative text"

customadmin_site = CustomadminAdminArea(name='CustomadminAdmin') 

class PostAdmin(admin.ModelAdmin):
	fieldsets = (
			('section 1', {
				'fields': ('title','author',),
				'description': "%s" % TEXT,
				}),
			('section 2', {
				'fields': ('slug',)
				}),
		)
	list_display=['category','title']	

customadmin_site.register(Post,PostAdmin)