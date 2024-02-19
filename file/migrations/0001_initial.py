# Generated by Django 5.0.1 on 2024-02-19 08:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publication_year', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('num_ratings', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='file_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file_type', models.CharField(choices=[('pdf', 'PDF'), ('slides', 'Slides'), ('doc', 'Doc')], max_length=50)),
                ('file', models.FileField(upload_to='docs/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='file.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
