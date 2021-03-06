from rest_framework import routers

from django.urls import include, path

from .rest_api.views import *

rest_router = routers.DefaultRouter()
rest_router.trailing_slash = "/?"  # added to support both / and slashless
rest_router.register(r'director', DirectorView)
rest_router.register(r'promoter', PromoterView)
rest_router.register(r'event_type', EventTypeView)
rest_router.register(r'event_day', EventDayView)
rest_router.register(r'race', RaceView)
rest_router.register(r'event', EventView)
rest_router.register(r'participant', ParticipantView)
rest_router.register(r'raceresult', RaceResultView)
rest_router.register(r'laptimes', LapTimesView)


app_name = 'rest_api'

urlpatterns = [
    path('', include(rest_router.urls)),
]
