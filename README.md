# django-environment-highlight

A Django application to visually distinguish the Django admin site for 
different environments like staging, 
development or live.
 
## Requirements
Tested with Django versions >= 2.2 (Should also work for earlier versions).

## Quick start

1. Add 'environment_highlight' to your INSTALLED_APPS setting.
   It is important to add 'environment_highlight' BEFORE 
    'django.contrib.admin':

    ```
    INSTALLED_APPS = [
        'environment_highlight',
        
        'django.contrib.admin',
        ...
    ]
    ```
  
2. Add this ENVIRONMENT_HIGHLIGHT dictionary to your settings.py.
   You can add environments as you like. The environment set 
   in ACTIVE_ENVIRONMENT will be displayed. It has to correspond to a key in the 
   ENVIRONMENTS dictionary. If ACTIVE_ENVIRONMENT is set to None, no environment 
   will be shown on the Django admin site. 
    ```
    ENVIRONMENT_HIGHLIGHT = {
        'ACTIVE_ENVIRONMENT' : 'staging',
        'ENVIRONMENTS' : {
            'staging': {
                'name': 'STAGING',
                'color': '#5BC0DE',
            },
            'development': {
                'name': 'DEVELOPMENT',
                'color': '#F0AD4E',
            },
            'live': {
                'name': 'LIVE',
                'color': '#79aec8;',
            }
        }
    }
    ```
3. Add 'environment_highlight.context_processors.environment_highlight_config'
to 'context_processors' in settings.py:
    ```
    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    ...
                    'environment_highlight.context_processors.environment_highlight_config',
                ],
            },
        },
    ]
    ```

