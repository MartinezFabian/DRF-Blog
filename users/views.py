from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from .serializers import CustomUserSerializer


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
