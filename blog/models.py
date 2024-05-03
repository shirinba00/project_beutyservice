from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.utils import timezone
from django.db.models import Avg
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from core.models import CustomUser


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub')
    sub_cat = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    datetime_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='category_blog/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:cat', args=[self.slug, self.id])



class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),

    )
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category, blank=True,)
    title = models.CharField(max_length=200,)
    title_english = models.CharField(max_length=200,)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True,)
    text = RichTextUploadingField(blank=True, null=True,)
    datetime_created = models.DateField(default=timezone.now,)
    datetime_modified = models.DateField(auto_now=True,)
    status = models.CharField(default='pub', choices=STATUS_CHOICES, max_length=3,)
    cover = models.ImageField(upload_to='covers/',)
    file = models.FileField(upload_to='files_post/', blank=True, null=True,)
    tags = TaggableManager(blank=True)
    view = models.ManyToManyField(get_user_model(), blank=True, related_name='post_view',)
    num_view = models.IntegerField(default=0,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])


