from django.contrib import admin
from .models import Posts, Comments
# Register your models here

class AdminPosts(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

class AdminComments(admin.ModelAdmin):
    list_display = ('commentaire', 'like')

admin.site.register(Posts, AdminPosts)
admin.site.register(Comments, AdminComments)

