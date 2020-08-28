# Generated by Django 3.1 on 2020-08-28 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0003_auto_20200828_1451'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faceDetector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('is_present', models.BooleanField(default=False)),
                ('class_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.class')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]