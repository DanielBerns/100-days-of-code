import os
from pathlib import Path
from dotenv import load_dotenv

base_path = Path(__file__).parent

app_identifier = 'athena'
app_data_path = Path('~', 'data', app_identifier, 'website').expanduser()
load_dotenv(Path(app_data_path, 'env'))

class ConfigException(Exception):
    pass

class Config(object):
    IDENTIFIER = app_identifier
    DATA_PATH = app_data_path    
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1123581235711'
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL') or 'DEBUG'
    PICTURES = Path(app_data_path, 'pictures')
    LOGS = Path(app_data_path, 'logs')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + str(Path(app_data_path, 'store', 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE=10
