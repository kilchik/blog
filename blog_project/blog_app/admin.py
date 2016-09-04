from django.contrib import admin
from .models import Article, Tag


class TagsInline(admin.TabularInline):
    model = Article.tags.through
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'cut', 'rest_text', 'pub_date']}),
    ]
    inlines = [TagsInline]
    list_display = ('title', '_get_tags', 'pub_date')

    def _get_tags(self, obj):
        return ', '.join(t.__str__() for t in Tag.objects.filter(article__id=obj.id))
    _get_tags.short_description = 'TAGS'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
