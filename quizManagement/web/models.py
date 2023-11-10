from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Student(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    image = models.ImageField(upload_to='students/', null=True)
    contact = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    userID = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Teacher(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    image = models.ImageField(upload_to='teachers/')
    contact = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    userID = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Classes(models.Model):
    className = models.CharField(max_length=150)
    classDescription = models.CharField(max_length=250, null=True)
    teacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.className


class Topics(models.Model):
    topicTitle = models.CharField(max_length=150)
    topicDescription = models.CharField(max_length=250, null=True)
    classID = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.topicTitle


class QuestionBank(models.Model):
    questionText = models.CharField(max_length=250)
    questionDescription = models.CharField(max_length=250)
    optionA = models.CharField(max_length=250)
    optionB = models.CharField(max_length=250)
    optionC = models.CharField(max_length=250)
    optionD = models.CharField(max_length=250)
    correctAnswer = models.CharField(max_length=100)

    def __str__(self):
        return self.questionText


class Question(models.Model):
    qbank_id = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)

    def __str__(self):
        return self.qbank_id.questionText


class Quizzes(models.Model):
    quizTitle = models.CharField(max_length=150)
    quizDescription = models.CharField(max_length=250, null=True)
    timeLimit = models.IntegerField()
    totalScore = models.IntegerField()
    dateCreated = models.DateTimeField(default=timezone.now)
    dateModified = models.DateTimeField(auto_now=True, null=True)
    topic_id = models.ForeignKey(Topics, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, null=True)

    def __str__(self):
        return self.quizTitle


class QuizRecord(models.Model):
    studentID = models.OneToOneField(Student, on_delete=models.CASCADE)
    quizID = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    dateTimeTaken = models.DateTimeField(auto_now_add=True, null=True)
    timeLeft = models.IntegerField(null=True)
    score = models.IntegerField(null=True)

    def __str__(self):
        return self.studentID + "(" + self.quizID + ")"


class Answers(models.Model):
    questionID = models.OneToOneField(Question, on_delete=models.CASCADE)
    quizRecordID = models.ForeignKey(QuizRecord, on_delete=models.CASCADE)
    answer = models.CharField(max_length=250, null=True)
    isCorrect = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.studentID + "(" + self.questionID + ")"
