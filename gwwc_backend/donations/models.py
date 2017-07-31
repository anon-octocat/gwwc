from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Donation(models.Model):
    """
    Users can track donations they've made to organizations, although they don't need to include the
    name of the org if they don't want.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO(JP) Could make these link to organization objects
    organization = models.CharField(max_length=200, default="")
    # TODO(JP) Don't assume USD for everyone
    amount = models.PositiveIntegerField()
    date = models.DateTimeField('date of donation')

    def __str__(self):
        return f"${self.amount} donation to {self.organization} on {self.date}"

    def serialize(self):
        return """{
    "organization": "%s",
    "amount": %f,
    "date": "%s",
}
    """ % (self.organization, self.amount, self.date)


class Income(models.Model):
    """
    User's annual income, in USD
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    amount = models.DecimalField(decimal_places=15, max_digits=30)

    def __str__(self):
        return f"${self.amount} per year income"


class Pledge(models.Model):
    """
    What percentage did the user pledge to donate
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    percentage = models.DecimalField(
        decimal_places=15,
        max_digits=30,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return f"A pledge to donate {self.percentage} of income per year"
