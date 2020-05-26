from django.apps import AppConfig


class SummerschoolConfig(AppConfig):
    name = 'summerschool'

    def ready(self):
        import summerschool.signals
