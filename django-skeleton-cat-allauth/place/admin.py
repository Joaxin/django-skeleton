from django.contrib import admin
from .models import place

@admin.register(place)
class placeAdmin(admin.ModelAdmin):
    list_display=['id','get_city_display','destination','address','rating','date','tag_list','notes']
    list_filter = ('date','rating')
    search_fields = ('city','destination','address','date','tags__name','notes')
    date_hierarchy = 'date'

    def tag_list(self, obj):
        return u", ".join(c.name for c in obj.tags.all())