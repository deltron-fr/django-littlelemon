from django.db import models
from django.core.exceptions import ValidationError

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guest = models.IntegerField()
    BookingDate = models.DateTimeField()

    def clean(self):
        if self.No_of_guest < 1:
            raise ValidationError("Number of guests must be at least 1.")
        
    def __str__(self):
        return f'{self.Name} - {self.No_of_guest} guests - {self.BookingDate}'

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
