from django.db import models

# Create your models here.


class customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=35)
    cust_address = models.CharField(max_length=37)
    cust_phone = models.IntegerField()
    def _str_(self):
        return self.cust_name

       


     