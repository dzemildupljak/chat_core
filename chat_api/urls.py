from django.urls import path
from chat_api.views import MessageApi

urlpatterns = [
    # path('users/', views.get_all_users),
    path('message-list/<int:sender>/<int:receiver>', MessageApi.as_view()),
    path('message/', MessageApi.as_view())
]
