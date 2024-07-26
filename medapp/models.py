from django.db import models
from django.contrib.auth import get_user, get_user_model
from medapp.utils import *
from datetime import datetime
from django.urls import reverse

class BaseMixin(models.Model):
    slug = models.SlugField(unique=True,editable=False,blank=True,null=True)
    created_at = models.DateField(auto_now=True,blank=True,null=True,)
    updated_at = models.DateField(auto_now=True,blank=True,null=True,)
    
    class Meta:
        abstract = True
    
class Category(BaseMixin):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            count = 0
            while Category.objects.filter(slug=self.slug).exists():
                count += 1
                self.slug = f"{slugify(self.title)}-{count}"
        super().save(*args, **kwargs)

class Tag(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Blog(BaseMixin):
    title = models.CharField(max_length=300)
    image = models.ImageField(null=True,blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='categoryBlogs')
    tag = models.ManyToManyField(Tag,related_name='categoryBlogs')
    writer = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            count = 0
            while Blog.objects.filter(slug=self.slug).exists():
                count += 1
                self.slug = f"{slugify(self.title)}-{count}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog', kwargs={"slug": self.slug})

class BlogSection(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blogSections')
    title = models.CharField(max_length=300)
    image = models.ImageField(null=True,blank=True)
    image2 = models.ImageField(null=True,blank=True)
    content = models.TextField()



class Comment(models.Model):
    description = models.TextField(null=True,blank=True)
    full_name = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=400,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    date = models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.full_name  

    
class Service(BaseMixin):
    title = models.CharField(max_length=300)
    image = models.ImageField(null=True,blank=True)
    content = models.TextField()
    image_at_detail = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            count = 0
            while Service.objects.filter(slug=self.slug).exists():
                count += 1
                self.slug = f"{slugify(self.title)}-{count}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service', kwargs={"slug": self.slug})

class ServiceSection(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='serviceSections')
    title = models.CharField(max_length=300)
    image = models.ImageField(null=True,blank=True)
    image2 = models.ImageField(null=True,blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title  
    
class Doctor(BaseMixin):
    full_name = models.CharField(max_length = 300)
    description = models.TextField()
    phone_number = models.CharField(max_length = 400)
    email = models.EmailField(null=True,blank=True)
    speciality = models.CharField(max_length=300)
    university = models.CharField(max_length=400)
    experience = models.TextField(null=True,blank=True)
    instagram = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    whatsapp = models.BooleanField(default=False)
    facebook = models.CharField(max_length=400,null=True,blank=True)
    short_exp = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('doctor', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
            count = 0
            while Doctor.objects.filter(slug=self.slug).exists():
                count += 1
                self.slug = f"{slugify(self.full_name)}-{count}"
        super().save(*args, **kwargs)

class Award(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='awards')
    name = models.CharField(max_length=900)
    description = models.TextField(null=True,blank=True)
    year = models.CharField(max_length=500,null=True,blank=True,default='')

    def __str__(self):
        return f'{self.doctor.full_name}-{self.name}'

class DoctorMessage(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length = 400)
    email = models.EmailField(null=True,blank=True)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    
class HomeSlider(models.Model):
    miniTitle = models.CharField(max_length=300,null=True,blank=True)
    title = models.CharField(max_length=300,null=True,blank=True)
    image = models.ImageField()
    in_home = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
class Message(models.Model):
    full_name = models.CharField(max_length=400)
    phone = models.CharField(max_length=400)
    subject = models.CharField(max_length=400)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name