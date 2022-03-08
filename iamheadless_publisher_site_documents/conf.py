from django.conf import settings as dj_settings

from .apps import IamheadlessPublisherSiteDocumentsConfig as AppConfig


class Settings:

    APP_NAME = AppConfig.name
    VAR_PREFIX = APP_NAME.upper()

    ITEM_TYPE = 'documents'

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
