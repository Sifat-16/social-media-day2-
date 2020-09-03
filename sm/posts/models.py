from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile

# Create your models here.
class Post(models.Model):
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/', blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author')
    liked = models.ManyToManyField(Profile, related_name='likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url

    def __str__(self):
        return str(self.content[:10])

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body[:10])

LIKE = (
    ('like', 'like'),
    ('unlike', 'unlike')
)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=6, choices=LIKE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


