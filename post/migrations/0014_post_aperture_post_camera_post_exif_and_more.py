# Generated by Django 4.1 on 2022-11-26 14:06

from django.db import migrations, models
import exiffield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0013_postmeta"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="aperture",
            field=models.FloatField(default=None, editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name="post",
            name="camera",
            field=models.TextField(default=None, editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name="post",
            name="exif",
            field=exiffield.fields.ExifField(default={}, editable=False),
        ),
        migrations.AddField(
            model_name="post",
            name="focal_length",
            field=models.FloatField(default=None, editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name="post",
            name="iso",
            field=models.IntegerField(default=None, editable=False),
        ),
        migrations.AddField(
            model_name="post",
            name="model",
            field=models.TextField(default=None, editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name="post",
            name="shutter_speed",
            field=models.FloatField(default=None, editable=False, max_length=100),
        ),
        migrations.DeleteModel(name="PostMeta",),
    ]