from django.db import models
from accounts.models import CustomUser
import datetime


class Schedule(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="Schedule_owner")
    summary = models.CharField("タイトル　※必須", max_length=20)
    date = models.DateField("日付　※必須")
    place = models.CharField("場所", max_length=20, blank=True)
    time = models.TimeField("時間", blank=True, null=True)
    detail = models.TextField("詳細", blank=True)
    author = models.CharField(max_length=20, default="あなた")
