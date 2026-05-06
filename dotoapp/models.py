from django.db import models

# Create your models here.
from django.db import models

class Logo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='logos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class WhatOurClientsSay(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='clients/profile/')
    box_image = models.ImageField(upload_to='clients/box/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


 

class NewOnOurReel(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reels/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "New On Our Reel"
        verbose_name_plural = "New On Our Reel"



from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='team/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "The People Behind The Craft"
        verbose_name_plural = "The People Behind The Craft"





class DigitalImpactStory(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='digital_stories/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Digital Impact Stories"
        verbose_name_plural = "Digital Impact Stories"



 
class CreativeContentPortfolio(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=150)
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

 

class AddYourWords(models.Model):
    name = models.CharField(max_length=150)
    review = models.TextField()
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
 



 

class SuccessStories(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='success_stories/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    


from django.db import models

class ContactLead(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




from django.utils.text import slugify

class OurBlog(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    intro = models.TextField()
    description = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
from ckeditor.fields import RichTextField
from django.utils.text import slugify
class ReadBlog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    image = models.ImageField(upload_to='blogs/')
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title