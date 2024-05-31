from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title


# class Test(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="test")
#
#     def __str__(self):
#         return self.title

class UserInfo(models.Model):
    user_no = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_birthyear = models.CharField(max_length=50)
    user_birthmonth = models.CharField(max_length=50)
    user_birthday = models.CharField(max_length=50)
    user_azurerole = models.BooleanField()
    user_blackrole = models.BooleanField()
    user_professionarea = models.CharField(max_length=50)
    user_workforunit = models.CharField(max_length=50)
    user_title = models.CharField(max_length=50)
    user_sociallinkedin = models.CharField(max_length=200)
    user_socialtwitter = models.CharField(max_length=200)
    user_socialfacebook = models.CharField(max_length=200)
    user_note = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user_info_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_infos")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'user'
