from django.contrib import admin
# Register your models here.
from .models import Post, Tag, Section

class CustomPost(admin.ModelAdmin):
	list_display=('title','section','pup_date')
	search_fields = ['section']
	list_filter = ['pup_date','tag']
admin.site.register(Post, CustomPost)
admin.site.register(Tag)
admin.site.register(Section)
