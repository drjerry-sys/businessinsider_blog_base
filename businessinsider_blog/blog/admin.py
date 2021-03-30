from django.contrib import admin
from .models import Post, Tag, Category, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('post_body', 'post_title')
    prepopulated_fields = {'slug':('post_title',)}
    raw_id_fields = ('category',)
    date_hierarchy = 'publish'
    list_filter = ('publish', 'post_title', 'status')
    list_display = ('post_title', 'category', 'popular', 'status')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('tag_name',)
    list_display = ('tag_name',)
    raw_id_fields = ('post',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)
    list_filter = ('category_name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('comment_message', )
    list_display = ('comment_name', 'comment_email')
    list_filter = ('created', 'active')