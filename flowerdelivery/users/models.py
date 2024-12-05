# Если вы используете `AbstractUser`, то ваша кастомная модель пользователя будет автоматически включать следующие стандартные поля:
#
# 1. `username` - уникальное имя пользователя.
# 2. `first_name` - имя пользователя.
# 3. `last_name` - фамилия пользователя.
# 4. `email` - адрес электронной почты.
# 5. `is_active` - флаг, указывающий, активен ли пользователь.
# 6. `is_staff` - флаг, указывающий, имеет ли пользователь доступ к админке.
# 7. `is_superuser` - флаг, указывающий, является ли пользователь суперпользователем.
# 8. `last_login` - дата и время последнего входа.
# 9. `date_joined` - дата и время регистрации пользователя.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    user_id = models.ForeignKey('self', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.username




# Create your models here.
