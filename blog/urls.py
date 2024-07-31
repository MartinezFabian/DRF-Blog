from django.urls import path
from .views import (
    AllPostList,
    PostDetail,
    UserPostList,
    CreatePost,
    UpdatePost,
    DeletePost,
)

urlpatterns = [
    path("all/", AllPostList.as_view(), name="all_posts"),
    path("user/", UserPostList.as_view(), name="user_posts"),
    path("create/", CreatePost.as_view(), name="create_post"),
    path("update/<int:pk>", UpdatePost.as_view(), name="update_post"),
    path("delete/<int:pk>", DeletePost.as_view(), name="delete_post"),
    path("detail/<slug:pk>", PostDetail.as_view(), name="detail_post"),
]
