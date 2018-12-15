import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__ (self):
        return self.question_text

    def was_public_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__ (self):
        return self.choice_text

class Client(models.Model):
    identity_card = models.CharField(max_length = 13)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length = 50)
    e_mail = models.CharField(max_length = 200)
    create_date = models.DateTimeField('create at')
    modify_date = models.DateTimeField('modify at')

    def __str__ (self):
        return self.cli_name

    def was_create_recently(self):
        return self.create_date >= timezone.now()-datetime.timedelta(days=1)
        
class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField('reservation date')
    people_quatity = models.IntegerField(default=1)
    menu_type = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)

    def __str__ (self):
        return self.reservation_date + self.people_quatity         