from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from ckeditor.fields import RichTextField


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    title = models.CharField(max_length=200)
    # slug = AutoSlugField(populate_from='title')
    slug = models.SlugField(max_length=200, default="", null=True, blank=True)
    thumbnail = models.ImageField(upload_to="blogs", null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    # content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post_authors')
    categories = models.ManyToManyField(Category)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta :
       ordering = ['-time']

    def __str__(self):
        return self.title



class Comment(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    time = models.DateTimeField(auto_now_add=True)

    class Meta :
       ordering = ['-time']

    def __str__(self):
        return self.content