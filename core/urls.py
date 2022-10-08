# app_name is important for the liveview and action decoraters
from django.urls import path

from core import views
from core.views import home, live_map, map_data

app_name = 'core'

# Automatically creates urlpatterns for all functions in views.py decorated with @liveview or @action.
urlpatterns = [
    path('', home),
    path('map', live_map),
    path('mapdata', map_data)

]