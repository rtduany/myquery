import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently():
		self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_text = models.CharField(max_length=200)
	date_pub = models.DateTimeField('date published')

	def __str__(self):
		return self.answer_text
