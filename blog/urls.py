from django.urls import path
from .views import PostUserList

urlpatterns = [
    path("user/", PostUserList.as_view(), name="posts_user"),
]
