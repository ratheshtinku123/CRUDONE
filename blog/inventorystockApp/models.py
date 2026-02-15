from django.db import models

# Create your models here.

class inventorystockdata(models.Model):
    Supplier_Name = models.CharField(max_length=100)
    Product_Name = models.CharField(max_length=100)
    Stock_Quantity = models.IntegerField()
    Purchase_Date = models.DateField()
    Reorder_Level = models.CharField(max_length=100)

    def __str__(self):
        return self.Supplier_Name

