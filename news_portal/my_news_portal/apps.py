from django.apps import AppConfig


class MyNewsPortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_news_portal'

    def ready(self):
        import my_news_portal.signals
