from django.urls import path
from .views import RegisterApi, UserApi


urlpatterns = [
    path('api/register', RegisterApi.as_view()),
    path('api/user-list/', UserApi.as_view()),
    path('api/user-list/<int:user_id>', UserApi.as_view()),
]
