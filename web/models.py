from django.db import models

# Create your models here.
class Entry(models.Model):
    name = models.CharField(max_length=30, default='Anonymous')
    amount = models.DecimalField(decimal_places=2, max_digits=100)
    message = models.TextField(max_length=100, default='', blank=True)
    paid = models.BooleanField(default=False)
    copy = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.amount}$ by {self.name} - {self.message} - Paid: {self.paid}'
