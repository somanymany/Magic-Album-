from django.contrib import admin
from .models import newposts,simdposts,simdfiles , NewsCategory , NewsPosts


class NewpostsAdmin(admin.ModelAdmin):
    list_display = ["title","add_time"]


class SimdPostsAdmin(admin.ModelAdmin):
    list_display = ["title","all_content","add_time"]


class SimdFilesAdmin(admin.ModelAdmin):
    list_display = ["title","file","add_time"]


class NewCategoryAdmin(admin.ModelAdmin):
    list_display = ["name","add_time"]


class NewPostsAdmin(admin.ModelAdmin):
    list_display = ["title","all_content","add_time"]


admin.site.register(NewsCategory, NewCategoryAdmin)
admin.site.register(NewsPosts, NewpostsAdmin)
admin.site.register(newposts, NewpostsAdmin)
admin.site.register(simdposts, SimdPostsAdmin)
admin.site.register(simdfiles, SimdFilesAdmin)