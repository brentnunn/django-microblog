from django.contrib import admin
from myblog.models import Post, Category


class CategoriesInLine(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoriesInLine]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
