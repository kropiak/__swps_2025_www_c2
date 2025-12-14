from django.contrib import admin
from .models import Category, Topic, Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['title', 'short_text', 'topic_with_category', 'created_at', 'created_by']
    list_filter = ['topic', 'created_by', 'topic__category']
    search_fields = ['title', 'text']

    @admin.display(description='Short text')
    def short_text(self, obj):
        return obj.__str__()

    @admin.display(description='Topic (Category)')
    def topic_with_category(self, obj):
        return f'{obj.topic.name} ({obj.topic.category.name})'


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created']
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


# a następnie zarejestrować (pokazano najprostszy przypadek)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
