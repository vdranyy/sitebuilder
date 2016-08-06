import sys
import os


from django.conf import settings


settings.configure(
    DEBUG=True,
    SECRET_KEY=os.environ.get('SECRET_KEY', '{{ secret_key }}'),
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    STATIC_URL='/static/',
)


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
