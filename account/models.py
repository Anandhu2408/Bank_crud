from django.db import models

class account(models.Model):
    account_holder=models.CharField(max_length=50)
    account_number=models.BigIntegerField()
    address=models.TextField()
    mobile_number=models.BigIntegerField()
    Account_balance=models.IntegerField()

    def __str__(self):
        return self.account_holder
