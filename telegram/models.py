from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    telegram_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.username