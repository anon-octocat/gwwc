import sys
import os

import yaml
from datetime import datetime
# Django initialization
os.environ["DJANGO_SETTINGS_MODULE"] = "gwwc_backend.settings"
import django
django.setup()
from django.contrib.auth.models import User
from django.utils import timezone
from donations.models import Income, Pledge

USAGE = "python load_dummy_data.py dummy_data.yaml"


def load_donations(user_db, user_data):
    for donation in user_data["donations"]:
        date_naive = datetime.strptime(donation["date"], "%Y/%m/%d")
        date = timezone.make_aware(date_naive)

        user_db.donation_set.create(
            organization=donation["organization"],
            amount=donation["amount"],
            date=date
        )


def load_data(data):
    """
    Take a dictionary with structure similar to that in dummy_data.yaml and load it into the
    database
    NB: This is a pretty fragile script
    """
    for username, user_data in data["users"].items():
        # TODO
        user_db = User.objects.create_user(username, user_data["email"], user_data["password"])
        user_db.first_name = user_data["first_name"]
        user_db.last_name = user_data["last_name"]
        user_db.income = Income(amount=user_data["income"])
        user_db.pledge = Pledge(percentage=user_data["pledge"])
        load_donations(user_db, user_data)
        user_db.save()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)
    with open(sys.argv[1]) as f:
        data = yaml.load(f)
    load_data(data)
