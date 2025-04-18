from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="아이디",
    )

    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput,
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            "username",           # 아이디
            "password1",          # 비밀번호
            "password2",          # 비밀번호 확인
            "email",              # 이메일
            "last_name",          # 성
            "first_name",         # 이름
            "gender",             # 성별
            "age",                # 나이
            "weekly_reading_time",# 주간 독서 시간
            "yearly_read_books",  # 연간 독서량
            "profile_image",      # 프로필 사진
        )
        labels = {
            "username": '아이디',                                # 아이디
            "email": '이메일',                                 # 이메일
            "last_name": '성',                                # 성
            "first_name": '이름',                             # 이름
            "gender": '성별',                                 # 성별
            "age": '나이',                                    # 나이
            "weekly_reading_time": '주간 독서 시간(시간)',      # 주간 독서 시간
            "yearly_read_books": '연간 독서량(권)',            # 연간 독서량
            "profile_image": '프로필 사진',                    # 프로필 사진
        }

class CustomUserChangForm(UserChangeForm):
    username = forms.CharField(
        label="아이디",
    )
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = (
            "username",           # 아이디
            "last_name",          # 성
            "first_name",         # 이름
            "email",              # 이메일
            "gender",             # 성별
            "age",                # 나이
            "weekly_reading_time",# 주간 독서 시간
            "yearly_read_books",  # 연간 독서량
            "profile_image",      # 프로필 사진
        )
        labels = {
            'last_name': '성',
            'first_name': '이름',
            'email': '이메일',
            'gender': '성별',
            'age': '나이',
            'weekly_reading_time': '주간 평균 독서 시간(시간)',
            'yearly_read_books': '연간 독서량(권)',
            'profile_image': '프로필 사진',
        }
