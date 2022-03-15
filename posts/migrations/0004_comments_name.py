# Generated by Django 3.2.9 on 2022-03-09 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
