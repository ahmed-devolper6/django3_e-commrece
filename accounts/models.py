from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here
DATA_TYPE = (
    ('home','home'),
    ('office','office'),
    ('acdemy','acdemy'),
    ('bussins','businss'),
)
class Proflie(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE , related_name='user_Proflie')
    image = models.ImageField(upload_to = 'users')
    code = models.BooleanField(default=False)
    code_used = models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.user)
@receiver(post_save , sender = User)
def geateproflie(sender, instance, created, **kwargs):
        if created:
            Proflie.objects.create(user=instance)
class Numbers(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE , related_name='User_number')
    type = models.CharField(choices=DATA_TYPE , max_length=10)
    phone_num = models.IntegerField(max_length=15)

class Address(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE , related_name='User_Adderrs')
    type = models.CharField(choices=DATA_TYPE , max_length=10)
    countery = CountryField()
    city = models.CharField(max_length=25)
    street = models.CharField(max_length=25)
    reogin = models.CharField(max_length=25)
    notes = models.CharField(max_length=250)
        