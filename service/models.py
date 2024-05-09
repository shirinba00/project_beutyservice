from django.db import models
from django.urls import reverse
from django.conf import settings
from core.models import CustomUser
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from uuid import uuid4
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.db.models import Avg



class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub')
    sub_cat = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    description = models.TextField(verbose_name='description')
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    picture_category = models.ImageField(upload_to='category_picture/', blank=True, null=True)
    # top_product = models.ForeignKey('TypeService', on_delete=models.SET_NULL, null=True, related_name='+')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service:category_sub', args=[self.slug])

class SampleGalleryPersonService(models.Model):
    person =models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=25,verbose_name='name_image',blank=True,null=True)
    description = models.TextField(max_length=1000,verbose_name='description_image',blank=True,null=True)
    image = models.ImageField(verbose_name='image',blank=True,null=True)
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=25,verbose_name='phone_number',)
    birth_date = models.DateField(verbose_name='birth_date', null=True, blank=True)
    gender = models.BooleanField(null=True, blank=True)
    information = models.TextField(verbose_name='information')
    picture = models.ImageField(upload_to='customer_picture/',verbose_name='customer_picture',
                                 null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    @property
    def first_name(self):
        return self.user.first_name
    class Meta:
        {'send_private_email', 'Can send email to user by the button '}

class Address(models.Model):
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postalcode= models.CharField(max_length=255)
    street= models.CharField(max_length=255)
     
class TypeService(models.Model):
    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),

    )
    name = models.CharField(max_length=255,verbose_name='name')
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True, verbose_name="slug_service")
    info = models.TextField()
    description = RichTextUploadingField(blank=True, null=True)
    icon = models.ImageField(upload_to='icon_typeservice/',null=True, blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2,verbose_name='price',null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True,verbose_name='datetime_created')
    datetime_modified = models.DateTimeField(auto_now=True,verbose_name='datetime_modified')
    picture = models.ImageField(upload_to='servicepicture/', verbose_name='servicepicture',null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,verbose_name='category_service',
                                       related_name='category_service')

    tags = TaggableManager(blank=True, verbose_name= 'tags_service')
   
    status = models.CharField(default='pub', choices=STATUS_CHOICES, max_length=3, verbose_name="status_service")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('service:detail_service', args=[self.slug])

class ReserveService(models.Model):
    service = models.ForeignKey(TypeService, on_delete=models.PROTECT, related_name='reserve_service')
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    phone = models.BigIntegerField(blank=True, null=True, unique=True)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.lastname

class PersonService(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='personservice_picture/',)
    phone= models.CharField(max_length=25, blank=True ,null=True,)
    information_short = models.TextField(blank=True ,null=True,)
    description = RichTextUploadingField(blank=True, null=True)
    instagram = models.CharField(max_length=50,blank=True ,null=True,)
    linkedin = models.CharField(max_length=50,blank=True ,null=True,)
    facebook = models.CharField(max_length=50,blank=True ,null=True,)
    pinterest = models.CharField(max_length=50,blank=True ,null=True,)
    typeservice = models.ForeignKey(TypeService,on_delete=models.PROTECT,blank=True,
                                         related_name='typeservice_personservice')
    tags = TaggableManager(blank=True, verbose_name= 'tags_service')
          
    def __str__(self):
        return self.phone

    def get_absolute_url(self):
        return reverse('service:detail_personservice', args=[self.id])

class Skill(models.Model):
    personservice = models.ForeignKey(PersonService,on_delete=models.PROTECT,blank=True,
                                         related_name='skill_personservice')
    title = models.CharField(max_length=255,)
    Skill_level = models.IntegerField()
    def __str__(self):
        return self.personservice.phone

class Comment(models.Model):
    COMMENT_STATUS_WAITING = 'w'
    COMMENT_STATUS_APPROVED = 'a'
    COMMENT_STATUS_NOT_APPROVED = 'na'
    COMMENT_STATUS = [
        (COMMENT_STATUS_WAITING, 'Waiting'),
        (COMMENT_STATUS_APPROVED, 'Approved'),
        (COMMENT_STATUS_NOT_APPROVED, 'Not Approved'),
    ]
    status = models.CharField(max_length=2, choices=COMMENT_STATUS, default=COMMENT_STATUS_WAITING)
    typeservice = models.ForeignKey(TypeService, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    text = models.TextField(verbose_name='Comment Text')
    datetime_created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name


