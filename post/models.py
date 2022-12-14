from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
from django.conf import settings
from django.utils import timezone
from django.db import models
import os
from django.dispatch import receiver
from exiffield.fields import ExifField
from exiffield.getters import exifgetter
# Create your models here.
AuthUser = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    image = models.ImageField(default=None, upload_to='users_posts')
    description = models.TextField(max_length=1000)
    date_publication = models.DateTimeField(auto_now_add=True)
    exif = ExifField(
        source='image',
    )

    def __str__(self):
        return self.title


    def publish(self):
        self.published_date = timezone.now()
        self.save()

def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

@receiver(models.signals.post_delete, sender=Post)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.image:
        _delete_file(instance.image.path)
    

class ImageData(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    camera = models.CharField(default=None, max_length=100, null=True, blank=True)
    model= models.CharField(default=None, max_length=100, null=True, blank=True)
    aperture = models.CharField(max_length=100, default=None, null=True, blank=True)
    shutter_speed = models.CharField(default=None, max_length=100, null=True, blank=True)
    focal_length = models.CharField( default=None, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.camera + "-" + self.post.title
