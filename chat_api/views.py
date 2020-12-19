from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import MessageSerializer
from .models import Message
# Create your views here.


class MessageApi(APIView):

    def get(self, request, sender=None, receiver=None):
        """
        Get all messages
        """
        messages = Message.objects.filter(
            sender_id=sender, receiver_id=receiver)
        revers_messages = Message.objects.filter(
            sender_id=receiver, receiver_id=sender)
        serializer = MessageSerializer(messages, many=True)
        reverse_serializer = MessageSerializer(revers_messages, many=True)
        serializer = list(serializer.data)
        serializer.extend(list(reverse_serializer.data))
        return Response(serializer)

    def post(self, request):
        """
        Create message with sender and receiver messages
        """
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
