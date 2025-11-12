from django.db import models

class UserName(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        app_label = 'greeting_app'
        verbose_name = "Имя пользователя"
        verbose_name_plural = "Имена пользователей"
    
    def __str__(self):
        return self.name