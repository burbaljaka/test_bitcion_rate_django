from django.urls import path
from .views import GetCurrentRate, GetLastRate

urlpatterns = [
    path("get_last/", GetLastRate.as_view(), name="get_last"),
    path("get_current/", GetCurrentRate.as_view(), name="get_current")
]