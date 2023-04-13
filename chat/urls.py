from django.urls import path
from rest_framework.authtoken import views

from chat.views import (ThreadCreateAPI, ThreadDestroyAPI, MessageListApi, UserThreadsListAPI, MessageCreateApi,
                        MessageUpdateApi, UserUnreadMessagesApi)


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('thread/', ThreadCreateAPI.as_view()),
    path('thread/<int:pk>/delete/', ThreadDestroyAPI.as_view()),
    path('thread/<int:pk>/messages/', MessageListApi.as_view()),
    path('user/<int:user_id>/threads/', UserThreadsListAPI.as_view()),
    path('user/<int:user_id>/new_message/', MessageCreateApi.as_view()),
    path('user/<int:user_id>/unread/', UserUnreadMessagesApi.as_view()),
    path('message/<int:pk>', MessageUpdateApi.as_view()),

]
