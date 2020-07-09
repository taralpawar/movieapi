from django.contrib import admin
from .models import MovieList, WatchList, RecommendList

admin.site.register(MovieList)
admin.site.register(WatchList)
admin.site.register(RecommendList)


# admin.site.register(Watch)
# admin.site.register(PopularList)
