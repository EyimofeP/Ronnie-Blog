# Generated by Django 3.0.3 on 2020-05-17 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200517_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='blog_photo',
            field=models.ImageField(blank=True, upload_to='assets/%Y/%m/%d/'),
        ),
    ]
