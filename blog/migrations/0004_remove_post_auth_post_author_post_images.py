# Generated by Django 4.2.3 on 2023-07-13 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_post_auth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='auth',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Post_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(default='', upload_to='img-post'),
            preserve_default=False,
        ),
    ]
