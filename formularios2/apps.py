from django.apps import AppConfig


class Formularios2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'formularios2'

    def ready(self):
        import formularios2.signals
