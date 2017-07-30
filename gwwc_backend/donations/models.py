from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Donation(models.Model):
    """
    TODO
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO(JP) Could make these link to organization objects
    organization = models.CharField(max_length=200, default="")
    # TODO(JP) Don't assume USD for everyone
    amount = models.PositiveIntegerField()
    date = models.DateTimeField('date of donation')

    def __str__(self):
        # TODO Check date formatting
        return f"${self.amount} donation to {self.organization} on {self.date}"


class Income(models.Model):
    """
    TODO
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=15, max_digits=30)

    def __str__(self):
        return f"${self.amount} per year income"


class Plege(models.Model):
    """
    TODO
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    percentage = models.DecimalField(
        decimal_places=15,
        max_digits=30,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        # TODO Check date formatting
        return "A pledge to donate {self.percentage} of income per year"
