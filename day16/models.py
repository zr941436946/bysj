from django.db import models

# Create your models here.

class deparment(models.Model):
    title = models.CharField(verbose_name="部门名",max_length=32,primary_key=True)
    ID =models.IntegerField(verbose_name="ID号")
class user(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=32,primary_key=True)
    password = models.CharField(verbose_name="密码",max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")
    title = models.ForeignKey(to="deparment",to_field="title",on_delete=models.SET_NULL,null=True,blank=True)



