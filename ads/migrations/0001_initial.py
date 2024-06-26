# Generated by Django 4.2.11 on 2024-03-31 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterAdvert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Фильтр',
                'verbose_name_plural': 'Фильтры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='ads.category', verbose_name='Родитель')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='Тема')),
                ('description', models.TextField(max_length=10000, verbose_name='Объявление')),
                ('file', models.FileField(blank=True, null=True, upload_to='callboard_file/', verbose_name='Файл')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.category', verbose_name='Категория')),
                ('filters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.filteradvert', verbose_name='Фильтр')),
                ('images', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='image.gallery', verbose_name='Изображения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
