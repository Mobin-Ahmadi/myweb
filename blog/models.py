from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Python','Python'),
        ('Solidworks','Solidworks'),
        ('Aspen','Aspen'),
        ('Articles','Articles'),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=600, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='post_images/',blank=True,null=True)
    attachment = models.FileField(upload_to='post_files/',blank=True,null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='blog')

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title
    
    @property
    def approved_comments(self):
        return self.comments.filter(approved=True)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'کامنت توسط {self.name} بر پست {self.post}'

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='certificates/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

