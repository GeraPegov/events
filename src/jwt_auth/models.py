from django.db import models

class AuthorizationModel(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(
        max_length=100,
        verbose_name='Логин'
    )
    password = models.CharField(
        max_length=100,
        verbose_name='Пароль'
    )