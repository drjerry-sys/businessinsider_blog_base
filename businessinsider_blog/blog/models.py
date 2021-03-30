from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    STATUS_CHOICE = (('draft', 'DRAFT'), ('publish', 'PUBLISH'))
    POPULAR = (('news', 'NEWS'), ('trending', 'TRENDING'), ('local', 'LOCAL'), ('retail', 'RETAIL'))
    post_title = models.CharField(max_length=100)
    post_body = models.TextField()
    post_image = models.FileField(null=True)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    popular = models.CharField(max_length=10, choices=POPULAR, default='news')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, unique=False, null=True, blank=True)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('news', args=[self.slug])

    def __str__(self):
        return self.post_title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.post_title)

class Tag(models.Model):
    tag_name = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, unique=False, on_delete=models.CASCADE, )

    def __str__(self):
        return self.tag_name

class Comment(models.Model):
    comment_name = models.CharField(max_length=25)
    comment_email = models.EmailField()
    comment_message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)