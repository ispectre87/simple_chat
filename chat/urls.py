from django.urls import path
from chat.views import (ThreadCreateAPI, ThreadDestroyAPI, MessageListApi, UserThreadsListAPI, MessageCreateApi,
                        MessageUpdateApi, UserUnreadMessagesApi)

urlpatterns = [
    path('thread/', ThreadCreateAPI.as_view()),
    path('thread/<int:pk>/', ThreadDestroyAPI.as_view()),
    path('thread/<int:thread_id>/messages/', MessageListApi.as_view()),
    path('user/<int:user_id>/threads/', UserThreadsListAPI.as_view()),
    path('user/<int:user_id>/message/', MessageCreateApi.as_view()),
    path('user/<int:user_id>/unread/', UserUnreadMessagesApi.as_view()),
    path('message/<int:pk>', MessageUpdateApi.as_view()),

]
