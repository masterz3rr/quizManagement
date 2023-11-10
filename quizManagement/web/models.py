from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Student(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    image = models.ImageField(upload_to='students/')
    contact = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    userID = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Teacher(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    image = models.ImageField(upload_to='teachers/')
    contact = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    userID = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Classes(models.Model):
    className = models.CharField(max_length=150)
    classDescription = models.CharField(max_length=250, null=True)
    teacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Topics(models.Model):
    topicTitle = models.CharField(max_length=150)
    topicDescription = models.CharField(max_length=250, null=True)
    classID = models.ForeignKey(Classes, on_delete=models.CASCADE)


class Quizzes(models.Model):
    quizTitle = models.CharField(max_length=150)
    quizDescription = models.CharField(max_length=250, null=True)
    timeLimit = models.IntegerField()
    totalScore = models.IntegerField()
    dateCreated = models.DateTimeField(default=timezone.now)
    dateModified = models.DateTimeField(auto_now=True, null=True)
    topic_id = models.ForeignKey(Topics, on_delete=models.CASCADE)


class QuestionBank(models.Model):
    questionText = models.CharField(max_length=250)
    questionDescription = models.CharField(max_length=250)
    optionA = models.CharField(max_length=250)
    optionB = models.CharField(max_length=250)
    optionC = models.CharField(max_length=250)
    optionD = models.CharField(max_length=250)
    correctAnswer = models.CharField(max_length=100)


class Question(models.Model):
    quiz_id = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    qbank_id = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)


class QuizRecord(models.Model):
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    quizID = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    dateTimeTaken = models.DateTimeField(auto_now_add=True, null=True)
    timeLeft = models.IntegerField(null=True)
    score = models.IntegerField(null=True)


class Answers(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    quizRecord_id = models.ForeignKey(QuizRecord, on_delete=models.CASCADE)
    answer = models.CharField(max_length=250, null=True)
    isCorrect = models.BooleanField(default=False, null=True)
