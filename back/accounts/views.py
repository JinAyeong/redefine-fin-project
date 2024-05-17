from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from dj_rest_auth.views import UserDetailsView

from .models import User
from .serializers import *


# 회원정보 조회
@api_view(['GET'])
def profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)