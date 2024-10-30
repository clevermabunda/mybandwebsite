from django.apps import AppConfig


class ThebandConfig(AppConfig):
    """
    Configuration for the 'theband' application.

    This class is used to configure the 'theband' Django application,
    setting the default primary key field type and application name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theband'
