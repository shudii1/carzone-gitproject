from django.contrib import admin

# Register your models here.
from pages.models import Team
# for working with html in admin or database
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    # for showing image in database
    def thumbnail(self, object):
        #adding image using format function passing photo url as src
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id','thumbnail', 'first_name',)
    search_fields = ('first_name','last_name','designation')
    #for filtering in search time
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
