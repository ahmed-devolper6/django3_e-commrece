from django.db import models
from utils.code_grente import grente_code
from django.utils import timezone
# Create your models here.
STATUS = (
    ('receieved','receieved'),
    ('processed','processed'),
    ('shiped','shiped'),
    ('delivered','delivered')
)
class Oders(models.Model):
    code = models.CharField(max_length=8 , default= grente_code)
    oder_time = models.DateTimeField(default=timezone.now)
    deilevry_time = models.DateTimeField()
    status = ''


class OderDeitl(models.Model):
    pass