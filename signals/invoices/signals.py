from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.consts import ORDER_PROCESSED, ORDER_DISPATCHED
from orders.models import Order


@receiver(post_save, sender=Order)
def send_order_notification(sender, instance, created, **kwargs):
    """
    Ugly signal receiver that works silently and is hard to discover or debug
    when issue occurs.
    """
    if instance.status == ORDER_PROCESSED:
        print(f"Creating invoice on order processed - id:{instance.id}")
    elif instance.status == ORDER_DISPATCHED:
        print(f"Sending invoice on order sent - id:{instance.id}")


from orders.signals import order_is_processed, order_sent


@receiver(order_is_processed)
def prepare_order_invoice(sender, order, **kwargs):
    """
    Explicit receiver for exposed signals from orders app, that can be
    used by this app to handle changes in the orders.
    """
    print(f"Preparing invoice for order id: {order.id}")


@receiver(order_sent)
def send_invoice(sender, order, **kwargs):
    print(f"Sending invoice for order id: {order.id}")
