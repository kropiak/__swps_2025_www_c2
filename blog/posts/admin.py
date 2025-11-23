from django.contrib import admin
from .models import Category, Topic, Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']

# a następnie zarejestrować (pokazano najprostszy przypadek)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Post, PostAdmin)
