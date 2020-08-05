from django.dispatch import Signal


order_is_processed = Signal(providing_args=["order"])
order_sent = Signal(providing_args=["order"])
