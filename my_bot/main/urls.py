from . import views
from django.urls import path

urlpatterns = [
    path('', views.choose_level, name = "level_choose"),
    path('level/<int:level_m>', views.main, name="main"),
]
