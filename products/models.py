from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from taggit.managers import TaggableManager
from django.utils import timezone

PRODECT_FLAG = (

    ('New' , 'New'),
    ('Sale' , 'Slae'),
    ('Fature' , 'Fature')

)

# product database.
class Products(models.Model):
    name = models.CharField(_('Name') , max_length=100)
    sku = models.IntegerField(_('SKU'))
    price = models.FloatField(_('Price'))
    image = models.ImageField(upload_to = 'proudcts')
    brand = models.ForeignKey('Brand' , on_delete= models.SET_NULL  , null=True , blank= True , verbose_name= _('Brand') , related_name='brand_product')
    rate = models.IntegerField(_('Rate'))
    dec = models.TextField(_('dec') , max_length=300)
    subtitle = models.CharField(_('subtitle') , max_length=150)
    tags = TaggableManager()
    flags = models.CharField( _('Flags'), max_length=10 , choices= PRODECT_FLAG ,)
    catgory = models.ForeignKey('Catgory' , on_delete= models.SET_NULL , null= True , blank= True , related_name='Catgory_prodcut', verbose_name=_('Catgory'))
    video_url = models.URLField(_('video_url'), null=True , blank=True)
    
    def __str__(self) -> str:
        return self.name
    

class ProductsImages(models.Model):
    products = models.ForeignKey(Products ,  verbose_name=_('Product_image') , on_delete= models.CASCADE)
    images = models.ImageField(_("image") , upload_to = 'productimages')
    def __str__(self) -> str:
        return str(self.products)


class Catgory(models.Model):
    name = models.CharField( _('Catgory_name') ,max_length=50)
    image = models.ImageField(_('Catgory_images') , upload_to = 'Cagtory')
    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField( _('Brand_name'),max_length=50)
    image = models.ImageField(_('Brand_images') , upload_to = 'Brand')
    def __str__(self) -> str:
        return self.name


class Reviw(models.Model):
    user = models.ForeignKey(User , on_delete= models.SET_NULL , null=True , blank=True , verbose_name= _('user'))
    products = models.ForeignKey(Products , on_delete=models.SET_NULL , null=True , blank= True,verbose_name=_('product' ))
    commnt = models.CharField(_('commnet') ,max_length=300)
    rate = models.IntegerField(_('Rate'))
    create_at = models.DateField(default=timezone.now, verbose_name=_('create_at'))
    def __str__(self) -> str:
        return str(self.products)