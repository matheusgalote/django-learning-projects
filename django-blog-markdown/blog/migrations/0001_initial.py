# Generated by Django 2.1.5 on 2021-07-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('category_img', models.ImageField(blank=True, null=True, upload_to='imgs/categories/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('cover_img', models.ImageField(blank=True, null=True, upload_to='imgs/covers/')),
                ('categories', models.ManyToManyField(related_name='posts', to='blog.Category')),
            ],
        ),
    ]
