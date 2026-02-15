from django.db import models

# Create your models here.

class AppointmentData(models.Model):
    Date = models.DateField()
    Time = models.TimeField()
    Client_Name = models.CharField(max_length=100)
    Contact_Number = models.CharField(max_length=100)
    Status = models.CharField(choices=[('Available', 'Available'),('Booked', 'Booked'),
                                       ('Cancelled', 'Cancelled')],default='Available',max_length=100)

    def __str__(self):
        return self.Client_Name
