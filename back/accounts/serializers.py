from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from allauth.account.adapter import get_adapter
from .models import User
from django.contrib.auth import get_user_model
UserModel = get_user_model()


# 회원정보 조회
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_active', 'is_staff', 'is_superuser')


# 회원정보 수정
class UserInfoserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'username',)


# 회원가입 custom serailizer
class CustomRegisterSerializer(RegisterSerializer):
    # 필요한 필드들을 추가합니다.
    # username = serializers.CharField(
    #     required=False,
    #     allow_blank=True,
    #     max_length=20
    # )
    name = serializers.CharField(required=False,allow_blank=True,max_length=10)
    # email = serializers.EmailField(
    #     required=False,
    #     max_length=30
    # )
    age = serializers.IntegerField()
    money = serializers.IntegerField()
    salary = serializers.IntegerField()

    # 해당 필드도 저장 시 함께 사용하도록 설정합니다. 
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            # 필드 추가
            'name': self.validated_data.get('name', ''),
            'email': self.validated_data.get('email', ''),
            'age': self.validated_data.get('age', ''),
            'money': self.validated_data.get('money', ''),
            'salary': self.validated_data.get('salary', ''),
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
    


# 회원정보 조회 custome serializer
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'name'):
            extra_fields.append('name')
        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        if hasattr(UserModel, 'money'):
            extra_fields.append('money')
        if hasattr(UserModel, 'salary'):
            extra_fields.append('salary')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)