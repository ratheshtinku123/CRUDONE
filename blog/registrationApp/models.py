from django.db import models


# Create your models here.

class RegistrationData(models.Model):
    Participant_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=15)
    Event_Name = models.CharField(max_length=100)
    Registration_Status = models.CharField(choices=[('Yes','Yes'),('No','No'),('Hold','Hold')])

    def __str__(self):
        return self.Participant_Name