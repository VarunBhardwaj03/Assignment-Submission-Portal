# Generated by Django 3.1.3 on 2020-11-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_info', '0002_auto_20201126_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='question_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]