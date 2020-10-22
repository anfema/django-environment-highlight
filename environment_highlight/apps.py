from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


class EnvironmentHighlightConfig(AppConfig):
    name = 'environment_highlight'

    try:
        active_environment = settings.ENVIRONMENT_HIGHLIGHT['ACTIVE_ENVIRONMENT']
        if active_environment:
            environment_color = settings.ENVIRONMENT_HIGHLIGHT['ENVIRONMENTS'][active_environment]['color']
            environment_name = settings.ENVIRONMENT_HIGHLIGHT['ENVIRONMENTS'][active_environment]['name']
    except (AttributeError, KeyError) as e:
        raise ImproperlyConfigured("Setting ENVIRONMENT_HIGHLIGHT missing or incorrect: {}".format(e))
