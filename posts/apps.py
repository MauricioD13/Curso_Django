from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Posts application settings

    Args:
        AppConfig ([type]): [description]
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    verbose_name = 'Posts'
