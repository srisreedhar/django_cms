from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display=["title"]
	#list_editable = ["title"] # editable & displylinks should not have same values.
	#list_display_links = ["timestamp"] # to make items clickable in list display
	list_filter = ["title"] # applying Filters to model admin
	search_fields = ["body","title"] # adding search field to Model Admin
	class Meta:
		model=Post

admin.site.register(Post,PostAdmin)
