from django.db import models


class Journey(models.Model):
    TRANSPORT_CHOICES = [
        ("Bus", "Bus"),
    ]
    departure = models.CharField(max_length=70)
    arrival = models.CharField(max_length=70)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    seats = models.PositiveIntegerField(default=30)
    duration = models.DurationField()
    transportation_choice = models.CharField(choices=TRANSPORT_CHOICES, max_length=20)

    def __str__(self):
        return f"From {self.departure} to {self.arrival}"


class Times(models.Model):
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE, null=True)
    departure_date = models.DateField()
    selected_time = models.TimeField()

    def __str__(self):
        return f"Ticket for ID {self.journey.id} : {self.departure_date}"


class Ticket(models.Model):
    time = models.ForeignKey(Times, on_delete=models.CASCADE)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    adult_ticket = models.PositiveIntegerField(default=1)
    child_ticket = models.PositiveIntegerField(default=0)

    def details(self):
        departure_time = self.time.departure_date
        arrival_time = self.time.selected_time + self.journey.duration
        duration = self.journey.duration

        return {
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "duration": duration,
        }

    def __str__(self):
        return f"Ticket for {self.journey.departure} to {self.journey.arrival} : {self.adult_ticket} Adult and {self.child_ticket} Children"
