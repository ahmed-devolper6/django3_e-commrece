from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logo')
    call_us = models.TextField(max_length=25)
    email_us = models.TextField(max_length=25)
    dec = models.TextField(max_length=200)
    fb_link = models.URLField(null=True, blank=True)
    tw_link = models.URLField(null=True, blank=True)
    li_link = models.URLField(null=True, blank=True)        #social_media links
    in_link = models.URLField(null=True, blank=True)
    pen_link = models.URLField(null=True, blank=True)
    subtitle = models.TextField(max_length=100)
    adderrs = models.TextField(max_length=250)

    app_link = models.URLField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name

