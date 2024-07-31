from django.urls import path
from .views import PostUserList, CreatePost

urlpatterns = [
    path("user/", PostUserList.as_view(), name="posts_user"),
    path("create/", CreatePost.as_view(), name="create_post"),
]
