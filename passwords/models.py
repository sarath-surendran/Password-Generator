from django.db import models
from users.models import MyUser

# Create your models here.

class SavePassword(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='save_password')
    password = models.CharField(max_length=200)

    def __srt__(self):
        return self.password