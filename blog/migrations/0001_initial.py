# Generated by Django 2.2.1 on 2019-05-22 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('subtitle', models.CharField(default='', max_length=100)),
                ('content', models.TextField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date updated')),
                ('views_number', models.IntegerField(default=0)),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
