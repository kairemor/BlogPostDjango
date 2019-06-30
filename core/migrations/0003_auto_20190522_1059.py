# Generated by Django 2.2.1 on 2019-05-22 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190122_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='description',
            new_name='job',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='photo'),
        ),
    ]
