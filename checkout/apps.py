from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    # overwrite ready method and import the signals
    def ready(self):
        import checkout.signals
