from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Thread, Message
from chat.serializers import (ThreadCreateSerializer, MessageGetSerializer, MessageCreateSerializer,
                              ThreadGetSerializer, MessageUpdateSerializer)
from chat.paginators import SimplePaginator


class TestView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        return Response([{'Status': 'Cool, you launched app'}])


class ThreadCreateAPI(generics.CreateAPIView):
    serializer_class = ThreadCreateSerializer


class ThreadDestroyAPI(generics.DestroyAPIView):
    serializer_class = ThreadCreateSerializer
    queryset = Thread.objects.all()


class MessageListApi(generics.ListAPIView):
    serializer_class = MessageGetSerializer
    pagination_class = SimplePaginator

    def get_queryset(self):
        thread_id = self.kwargs.get('pk')
        return Message.objects.filter(thread_id=thread_id)


class UserThreadsListAPI(generics.ListAPIView):
    serializer_class = ThreadGetSerializer
    pagination_class = SimplePaginator

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Thread.objects.filter(participants__in=[user_id])


class UserUnreadMessagesApi(generics.ListAPIView):
    serializer_class = MessageGetSerializer
    pagination_class = SimplePaginator

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Message.objects.filter(sender__in=[user_id], is_read__in=[False])


class MessageCreateApi(generics.CreateAPIView):
    serializer_class = MessageCreateSerializer

    def post(self, request, *args, **kwargs):
        request.data['sender'] = kwargs.get('user_id')
        return self.create(request, *args, **kwargs)


class MessageUpdateApi(generics.UpdateAPIView):
    serializer_class = MessageUpdateSerializer
    queryset = Message.objects.all()
