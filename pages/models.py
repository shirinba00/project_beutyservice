from django.db import models

from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField



class AboutUS(models.Model):
    title = models.CharField(max_length=200)
    text_short = models.TextField()
    information = RichTextUploadingField(blank=True, null=True)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='covers_about/', blank=True, null=True)
    file = models.FileField(upload_to='files_aboutus/', blank=True, null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.BigIntegerField(blank=True, null=True, unique=True, )
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    customers_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


# class ContactUs(models.Model):
#     title = models.CharField(max_length=100, blank=True, null=True)
#     text = RichTextUploadingField(blank=True, null=True)
#     datetime_created = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.title

 
