from django.db import models

# Create your models here.


class User(models.Model):
    email=models.EmailField(null=True,verbose_name='邮箱')
    upwd=models.CharField(max_length=20,verbose_name='密码')
    def __str__(self):
        return self.email
    class Meta:
        db_table='user'
        verbose_name='用户'


