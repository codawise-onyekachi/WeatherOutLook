from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.index)
# ]


urlpatterns = [
    path('', views.index, name='index1'),
    path('add_alert/', views.add_alert, name='add_alert'),
    path('check_weather/', views.check_weather, name='check_weather'),
]
