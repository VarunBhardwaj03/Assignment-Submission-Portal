# Generated by Django 4.0.6 on 2023-04-27 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignment_info', '0009_cname_secret_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reg_users', to='assignment_info.cname')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
