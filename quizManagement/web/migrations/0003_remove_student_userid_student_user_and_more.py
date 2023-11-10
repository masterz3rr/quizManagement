# Generated by Django 4.2.7 on 2023-11-09 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_classes_questionbank_rename_user_id_student_userid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='userID',
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='answers',
            name='isCorrect',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='classDescription',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='quizrecord',
            name='dateTimeTaken',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='quizrecord',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='quizrecord',
            name='timeLeft',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='quizzes',
            name='dateModified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='quizzes',
            name='quizDescription',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='topics',
            name='topicDescription',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
