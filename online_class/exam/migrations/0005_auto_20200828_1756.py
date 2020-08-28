# Generated by Django 3.1 on 2020-08-28 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
        ('exam', '0004_auto_20200828_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examanswers',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_answer', to='assignment.student'),
        ),
    ]