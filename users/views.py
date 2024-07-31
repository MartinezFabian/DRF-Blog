from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import CustomUserSerializer
from users.models import CustomUser


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            if user:
                token = Token.objects.create(user=user)
                json_user = serializer.data

                return Response(
                    {"token": token.key, "user": json_user},
                    status=status.HTTP_201_CREATED,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = get_object_or_404(CustomUser, email=request.data["email"])

        if not user.check_password(request.data["password"]):
            return Response(
                {"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST
            )

        token, created = Token.objects.get_or_create(user=user)
        serializer = CustomUserSerializer(instance=user)
        json_user = serializer.data

        return Response(
            {"token": token.key, "user": json_user}, status=status.HTTP_200_OK
        )
