# Generated by Django 2.2 on 2019-07-15 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_auto_20190715_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
