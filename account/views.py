from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework import permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
# Register API


class RegisterApi(generics.GenericAPIView):
    permission_classes = [AllowAny]
    # permission_classes = (AllowAny,)
    # permission_classes = AllowAny
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "message": "User Created Successfully. \
                        Now perform Login to get your token",
        })


class UserApi(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, user_id=None):
        if user_id is not None:
            user = User.objects.get(id=user_id)
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        else:
            all_users = User.objects.all()
            serializer = UserSerializer(all_users, many=True)
            return Response(serializer.data)
