# Generated by Django 5.0.6 on 2024-07-08 11:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandscapeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Select an image file', upload_to='landscape_images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='image', upload_to='posts/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Enter the category name', max_length=255),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a description of the photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(help_text='Select an image file', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(help_text='Enter the photo title', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='Enter the post content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Enter the post title', max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('title', 'category')},
        ),
    ]