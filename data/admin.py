
from django.contrib import admin

from .models import Family,Member,Ward





@admin.action(description='Mark selected person as Family head')
def make_head(modeladmin, request, queryset):
    queryset.update(status='H')


    raw_id_fields = ('family',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'status','job','age','blood_group','family']
    list_filter=['family']
    search_fields=['name','family','blood_group']
    ordering = ['family']
    actions = [make_head]
    search_fields = ('name_of_family_head',)
    raw_id_fields = ('family',)


admin.site.register(Family)
admin.site.register(Ward)
admin.site.register(Member,ArticleAdmin)
