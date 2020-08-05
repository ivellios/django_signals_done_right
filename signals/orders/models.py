from django.db import models

from .consts import ORDER_CREATED, ORDER_PROCESSED, ORDER_DISPATCHED
# Create your models here.
from .signals import order_is_processed, order_sent


class Order(models.Model):
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=40, default=ORDER_CREATED)

    def process(self, save=True):
        self.status = ORDER_PROCESSED
        if save:
            self.save(update_fields=["status"])
            order_is_processed.send(sender=self.__class__, order=self)

    def send(self, save=True):
        self.status = ORDER_DISPATCHED
        if save:
            self.save(update_fields=["status"])
            order_sent.send(sender=self.__class__, order=self)
