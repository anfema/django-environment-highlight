from django.conf import settings


def environment_highlight_config(request):
    active_environment = settings.ENVIRONMENT_HIGHLIGHT['ACTIVE_ENVIRONMENT']
    if active_environment:
        return {
            'ACTIVE_ENVIRONMENT' : active_environment,
            'ENVIRONMENT_COLOR': settings.ENVIRONMENT_HIGHLIGHT['ENVIRONMENTS'][active_environment]['color'],
            'ENVIRONMENT_NAME': settings.ENVIRONMENT_HIGHLIGHT['ENVIRONMENTS'][active_environment]['name']
        }
    else:
        return {
            'ACTIVE_ENVIRONMENT' : active_environment,
    }

