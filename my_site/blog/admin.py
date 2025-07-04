from django.contrib import admin
from .models import Post, Author, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('title', 'date')
    list_filter = ('title', 'date', 'author','tag')



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', "last_name")

class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)



# Register your models here.
