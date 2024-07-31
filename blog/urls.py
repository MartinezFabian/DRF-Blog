from django.urls import path
from .views import PostUserList, CreatePost, UpdatePost

urlpatterns = [
    path("user/", PostUserList.as_view(), name="posts_user"),
    path("create/", CreatePost.as_view(), name="create_post"),
    path("update/<int:pk>", UpdatePost.as_view(), name="update_post"),
]
