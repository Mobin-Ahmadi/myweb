from django.contrib import admin
from .models import Post, Comment,Certificate


admin.site.register(Comment)
admin.site.register(Certificate)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    