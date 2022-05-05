from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# from twilio.rest import Client

class User(AbstractUser):
    @property
    def is_employee(self):
        if hasattr(self, 'employee'):
            return True
        return False

class Book(models.Model):
    bookname=models.CharField(max_length=60, blank=True, null=True)
    author=models.CharField(max_length=60, blank=True, null=True)
    publication=models.CharField(max_length=60, blank=True, null=True)
    bookid = models.BigIntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.bookname)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_id=models.BigIntegerField()
    name=models.CharField(max_length=60, blank=True, null=True)
    phone=models.BigIntegerField(blank=True, null=True)
    department=models.CharField(max_length=60, blank=True, null=True)
    email=models.EmailField(blank=True, null=True)
    address=models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        '''if self.name==None:
            return str(self.card_id)
        else:
            return str(self.name) + ' : ' + str(self.card_id)'''
        return str(self.name)

class BookRecord(models.Model):
    bk=models.ManyToManyField(Book)
    bookid = models.BigIntegerField(null=True)
    bookname=models.CharField(max_length=60, blank=True, null=True)
    issuedDate=models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.bookname)

class Record(models.Model):
    emp = models.ManyToManyField(Employee)
    ids=models.IntegerField(default=0)
    card_id=models.BigIntegerField()
    name=models.CharField(max_length=60, blank=True, null=True)
    department=models.CharField(max_length=60, blank=True, null=True)
    date=models.DateField(default=datetime.date.today)
    # time_in=models.TimeField(default=datetime.datetime.now())
    # time_out=models.TimeField(blank=True, null=True)
    status=models.TextField(max_length=100)

    def __str__(self):
        return str(self.name) + ' : ' + str(self.date)


class EmpLeaveRequests(models.Model):
    remp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    date_from = models.DateField(max_length= 100, default=None)
    date_to = models.DateField(max_length=100, default=None)
    status = models.CharField(max_length=100, null=True)

class AppStatus(models.Model):
    leaveApp = models.ForeignKey(EmpLeaveRequests, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True)

class Notification(models.Model):
    content = models.CharField(max_length=1000, null=True)
    date=models.DateField(default=datetime.date.today)

class Tickets(models.Model):
    temp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    date = models.DateField(max_length= 100, default=None)
    status = models.CharField(max_length=100, null=True)

class MergeRecords(models.Model):
    book = models.CharField(max_length=50, default=None)
    student = models.CharField(max_length=100, default=None)

# class Score(models.Model):
#     #integer field
#     test_result = models.PositiveIntegerField()

#     #string representation
#     def __str__(self):
#         return str(self.test_result)

#     #save method
#     def save(self, *args, **kwargs):
#         #if test_result is less than 80 execute this
#         if self.test_result < 80:
#             #twilio code
#             account_sid = 'ACc0729c27fcc805834a08d88cec9d22fb'
#             auth_token = 'eb37225daf481d345f6f94b32d7a348e'
#             client = Client(account_sid, auth_token)

#             message = client.messages.create(
#                                         body=f'Hi, your test result is {self.test_result}. Great job',
#                                         from_='+15076398787',
#                                         to='+9779843507304' 
#                                     )

#             print(message.sid)
#         return super().save(*args, **kwargs)