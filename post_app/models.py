
from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
 

class Section(models.Model):
    title = models.CharField(max_length=200)
    mainPicture = models.ImageField()
    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.tag_name


class Post(models.Model):

    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    pup_date = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey(Section)
    tag = models.ManyToManyField(Tag,blank=True)


    def __str__(self):
        return self.title
    class Meta:
       ordering = ["-pup_date"]
