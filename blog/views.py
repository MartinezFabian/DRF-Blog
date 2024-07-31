from rest_framework import generics
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import PostSerializer
from .models import Post


# Create your views here.


class PostUserList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class CreatePost(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        # Asocia el nuevo post con el usuario autenticado
        serializer.save(author=self.request.user)


class UpdatePost(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
