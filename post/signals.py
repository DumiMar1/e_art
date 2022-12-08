from django.db.models.signals import post_save
from django.dispatch import receiver
from post.models import Post, ImageData
from exiffield.fields import ExifField
from exiffield.getters import exifgetter


@receiver(post_save, sender=Post)
def create_image_data(sender, instance, created, **kwargs):
    if created:
        ImageData.objects.create(
            post=instance,
            camera = instance.exif['Make']['val'],
            model=instance.exif['Model']['val'],
            aperture=instance.exif['FNumber']['val'],
            shutter_speed=instance.exif['ShutterSpeedValue']['val'],
            focal_length=instance.exif['FocalLength']['val'],

            )

