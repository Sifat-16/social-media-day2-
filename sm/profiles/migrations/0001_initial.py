# Generated by Django 3.0.9 on 2020-09-01 18:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('profile_pic', models.ImageField(default='avatar.png', upload_to='profile/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('cover_pic', models.ImageField(default='avatar.png', upload_to='cover/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('profession', models.CharField(default='No profession Added', max_length=250)),
                ('interest', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male & Female', max_length=6)),
                ('bio', models.TextField(default='No bio Added')),
                ('country', models.CharField(blank=True, max_length=100)),
                ('language', models.CharField(default='English', max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('friends', models.ManyToManyField(related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]