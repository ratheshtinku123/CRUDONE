from django.db import models
from django.db.models.enums import Choices


# Create your models here.

class TicketTracker(models.Model):
    Customer_Name = models.CharField(max_length=100)
    Vehicle_No = models.CharField(max_length=100)
    Title = models.CharField(max_length=120)
    Description = models.TextField()
    Priority = models.CharField(choices=[('High','High'),('Medium','Medium'),('Low','Low')])

    def __str__(self):
        return self.Customer_Name