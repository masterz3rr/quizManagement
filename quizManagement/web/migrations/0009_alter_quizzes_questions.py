# Generated by Django 4.2.7 on 2023-11-10 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_remove_answers_studentid_remove_question_quiz_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizzes',
            name='questions',
            field=models.ManyToManyField(null=True, to='web.question'),
        ),
    ]