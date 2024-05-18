from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from dj_rest_auth.views import UserDetailsView

from .models import User
from .serializers import ProfileSerializer, UserInfoserializer, CustomRegisterSerializer


# 회원정보 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


# # 회원정보 수정
# @api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
# def profile_info(request, username):
#     if request.user.username == username:
#         if request.method == 'GET':
#             user = get_object_or_404(get_user_model(), username=username)
#             serializer = UserInfoserializer(user)
#             return Response(serializer.data)
            
#         elif request.method == 'PUT':
#             user = get_object_or_404(get_user_model(), username=username)
#             serializer = UserInfoserializer(instance=user, data=request.data, partial=True)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save(user=request.user)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# # 회원 탈퇴
# def profile_delete(request):
#     request.user.delete()
#     return Response({'delete': '탈퇴가 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
