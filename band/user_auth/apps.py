from django.apps import AppConfig


class UserAuthConfig(AppConfig):
    """
    Configuration for the 'user_auth' application.

    This class manages the configuration settings for the 'user_auth'
    Django application, including the default primary key field type 
    and the application name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_auth'
