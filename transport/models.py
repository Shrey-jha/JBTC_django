
from django.db import models

class LoadInfo(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    size = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=200)
    drop_location = models.CharField(max_length=200)
    date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    time_of_pickup = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.weight}kg"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name