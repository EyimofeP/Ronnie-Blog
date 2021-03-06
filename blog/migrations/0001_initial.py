# Generated by Django 3.0.3 on 2020-05-11 23:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_content', models.TextField()),
                ('blog_time', models.DateTimeField(default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
                ('blog_url', models.SlugField(max_length=200)),
                ('short_description', models.CharField(max_length=200)),
                ('blog_author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='author.Author')),
            ],
        ),
    ]
