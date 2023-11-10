# Generated by Django 4.2.7 on 2023-11-10 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0004_rename_user_student_usertype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='userType',
            new_name='userID',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='userID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
