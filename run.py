from src import create_app
import os

settings_module = os.getenv('APP_SETTINGS_MODULE')
create_app(settings_module)