# Generated by Django 4.1 on 2022-11-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0015_alter_post_shutter_speed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="iso",
            field=models.CharField(default=None, editable=False, max_length=100),
        ),
    ]