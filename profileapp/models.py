from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') #이 프로필의 주인이 누구인지 정하기/User객체와 연결/User객체가 사라질때 file도 사라지도록/

    image = models.ImageField(upload_to='profile/', null=True) #
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)