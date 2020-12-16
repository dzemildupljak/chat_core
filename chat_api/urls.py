from django.urls import path
from chat_api.views import MessageView

urlpatterns = [
    # path('users/', views.get_all_users),
    path('message-list/<int:sender>/<int:receiver>', MessageView.as_view()),
    path('message/', MessageView.as_view())
]
