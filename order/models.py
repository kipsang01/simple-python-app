import environ
import logging

from django.contrib.auth.models import User
from django.db import models

from sms_service.service import send_sms

logger = logging.getLogger(__name__)

env = environ.Env()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    message_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item} - {self.customer.user.username}"

    def send_notification(self):
        order_summary = f"Item: {self.item} - Amount:{self.amount}"
        message = (f"Hello {self.customer.user.username}, Your Order {order_summary}"
                   f" has been received please be patient while it's being processed")

        recipients = [self.customer.phone_number]
        response = send_sms(recipients, message)
        if response['SMSMessageData']['Recipients'][0]['statusCode'] == 101:
            self.message_sent = True
            self.save()