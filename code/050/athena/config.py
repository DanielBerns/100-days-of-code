import os
from pathlib import Path
base = Path('~', 'db', 'athena').expanduser
database = Path(base, 'app').with_suffix('.db')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '112358132134'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + str(database)
 
