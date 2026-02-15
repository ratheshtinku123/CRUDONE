from django.db import models

# Create your models here.

class ExpenseTracker(models.Model):
    Date = models.DateField()
    Amount = models.CharField(max_length=100)
    Category = models.CharField(max_length=200)
    Payment_Mode = models.CharField(choices=[('UPI','UPI'),('Cash','Cash'),('Credit','Credit'),
                                             ('Debit','Debit')],default='UPI',max_length=100)

    Optional_Notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Category

