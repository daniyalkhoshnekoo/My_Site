from django.contrib import admin
from .models import Post,Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','counted_views','status','created_date','published_date')
    list_filter = ('status','counted_views')
    search_fields = ('title','content')
admin.site.register(Post, PostAdmin)
admin.site.register(Category)