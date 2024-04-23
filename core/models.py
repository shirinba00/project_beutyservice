from datetime import timedelta, timezone
import random
import string
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
 
    def __str__(self):
        return self.email
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = "Customuser"
        verbose_name_plural = "Customuser"

# Modify the related_name for groups and user_permissions in CustomUser model
CustomUser.groups.field.related_name = 'customuser_groups'
CustomUser.user_permissions.field.related_name = 'customuser_user_permissions'
    



class OTPRequestQuerySet(models.QuerySet):
     def is_valid(self,receiver,request,password):
          current_time = timezone.now() 
          return self.filter (
               receiver = receiver,
               request_id = request,
               password=password,
               created__lt = current_time,
               created__gt = current_time - timedelta(seconds =120),

          ).exists()



class OTPManager(models.Manager):

    def get_queryset(self):
        return OTPRequestQuerySet(self.model,self._db)
    
    def is_valid(self,receiver,request,password):
        return self.get_queryset().is_valid(receiver,request,password)
    

    def generate(self,data):
        otp = self.model(channel=data['channel'],receiver = data['receiver'])
        otp.save(using=self._db)
        return otp
    
    def generate_otp():
        rand = random.SystemRandom()
        digits = rand.choices(string.digits,k=4)
        return ''.join(digits)
        


class OTPRequest(models.Model):
    class OtpChannel(models.TextChoices):
        PHONE = 'Phone'
        EMAIL = 'E_mail'

    request_id = models .UUIDField(primary_key = True,editable = False,default = uuid.uuid4)
    channel =  models.CharField(max_length = 10 ,choices =OtpChannel.choices,default=OtpChannel.PHONE)
    receiver = models.CharField(max_length = 50)
    password = models.CharField(max_length = 4 , default = OTPManager.generate_otp )
    created = models.DateTimeField(auto_now_add=True,editable = False)

    objects= OTPManager()