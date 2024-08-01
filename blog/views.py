from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from django.db.models.query_utils import Q
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import PostSerializer
from .models import Post


# Create your views here.

# all users


class AllPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        slug_query = self.kwargs.get("pk")
        return get_object_or_404(Post, slug=slug_query)


class PostSearch(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("s")

        return Post.objects.filter(
            Q(title__icontains=search_term)
            | Q(excerpt__icontains=search_term)
            | Q(content__icontains=search_term)
        )


# only authenticated users


class CreatePost(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        # Asocia el nuevo post con el usuario autenticado
        serializer.save(author=self.request.user)


class UserPostList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class UpdatePost(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class DeletePost(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
