from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    gender_choices = [
        ('남성', '남성'),
        ('여성', '여성'),
    ]
    gender = models.CharField(max_length=3, choices=gender_choices, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    weekly_reading_time = models.FloatField(null=True, blank=True, help_text="주간 평균 독서 시간(시간)")
    yearly_read_books = models.PositiveIntegerField(null=True, blank=True, help_text="연간 독서량(권)")
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
