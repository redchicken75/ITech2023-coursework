from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNum =  models.CharField(max_length=14)
    address = models.CharField(max_length=128)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    # bookingStatus: true = expired booking, false = pending booking
    bookingID = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    numberOfPeople = models.IntegerField()
    notes = models.CharField(max_length=1000)
    bookingStatus = models.BooleanField()

    def __str__(self):
        return str(self.bookingID)


class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.reviewID)