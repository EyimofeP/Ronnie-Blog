# Generated by Django 3.0.3 on 2020-06-02 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200602_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='blog_photo',
            field=models.ImageField(blank=True, default='./media/default.jpg', upload_to='assets/%Y/%m/%d/'),
        ),
    ]
