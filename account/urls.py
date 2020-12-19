from django.conf.urls import url
from django.urls import path, include
from .views import RegisterApi, UserApi


urlpatterns = [
    path('api/register', RegisterApi.as_view()),
    path('api/user-list', UserApi.as_view())
]
