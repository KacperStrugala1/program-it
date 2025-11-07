from django.db import models

class Scores(models.Model):
    pk = models.DecimalField()
    points = models.DecimalField(
        max_digits=999999999
    )

    def __str__(self):
        return f"Your points: {self.points}"