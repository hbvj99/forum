from django.contrib import admin
from discussions.models import Discussion, Comment


class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'updated', 'timestamp', 'category', 'img')
    list_filter = ('user', 'updated', 'timestamp', 'category')
    search_fields = ('title', 'content', 'category')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'post')
    list_filter = ('user', 'timestamp')
    search_fields = ('content',)


admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.site_header = 'DJANGO FORUM'

