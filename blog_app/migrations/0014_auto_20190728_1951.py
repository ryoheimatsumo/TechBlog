# Generated by Django 2.2 on 2019-07-28 10:51

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0013_auto_20190715_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]