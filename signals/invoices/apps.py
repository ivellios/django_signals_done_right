from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    name = "invoices"

    def ready(self):
        import invoices.signals
