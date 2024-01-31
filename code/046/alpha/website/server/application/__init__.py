import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import uuid

from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


from config import Config

class T:
    lan = 'en'
    
    LOGIN_MESSAGE = 'Please log in to access this page.'
    DIFFERENT_USERNAME = 'Please use a different username'
    NO_USER_CREDENTIALS = 'Please include username and password fields: '
    STARTED = 'Started'
    YOUR_POST_IS_LIVE_NOW = 'Your post is live now!'
    INDEX = 'Index'
    EACH_USER_FOLLOWS_HER_POSTS = 'Each user follows her posts'
    HELP = 'HELP'
    NOW_YOU_ARE_FOLLOWING_THE_POSTS_BY = 'Now, you are following the posts by '
    USER_NOT_FOUND = 'User not found '
    YOU_HAVE_STOPPED_FOLLOWING_THE_POST_BY = 'You have stopped following the posts by '
    ALL_THE_POSTS = 'All the posts'
    MESSAGE_SENT = 'Message sent'
    SEND_MESSAGE = 'Send message'
    MESSAGES = 'Messages'
    MESSAGES_LIST = 'Messages list',
    SEND = 'Send'
    ACCEPT = 'Accept'
    USER = 'User'
    PASSWORD = 'Password'
    REPEAT_PASSWORD = 'Repeat password'
    ABOUT_ME = 'About me'
    INVALID_USERNAME_OR_PASSWORD = 'Invalid username or password'
    SIGN_IN = 'Sign in',
    REGISTER = 'Register user'
    BETWEEN_10_to_32_CHARACTERS = 'Input must be 10 to 32 characters long'
    MESSAGES = 'Messages'
    MESSAGE = 'Message'
    MESSAGES_LIST = 'Messages list'
    WRITE = 'Write'
    
es = {T.LOGIN_MESSAGE: 'Por favor, acceda a esta página con usuario y contraseña.',
      T.DIFFERENT_USERNAME: 'Por favor, use un nombre de usuario distinto.',
      T.NO_USER_CREDENTIALS: 'Por favor, incluya usuario y contraseña.',
      T.STARTED: 'Comenzamos!',
      T.YOUR_POST_IS_LIVE_NOW: 'Tu contenido está publicado!',
      T.INDEX: 'Indice',
      T.EACH_USER_FOLLOWS_HER_POSTS: 'Cada usuario observa sus publicaciones!',
      T.HELP : 'Ayuda',
      T.NOW_YOU_ARE_FOLLOWING_THE_POSTS_BY : 'Ahora estas observando las publicaciones de ',
      T.USER_NOT_FOUND : 'Usuario no encontrado: ',
      T.YOU_HAVE_STOPPED_FOLLOWING_THE_POST_BY : 'Has dejado de observar las publicaciones de ',
      T.ALL_THE_POSTS : 'Todas las publicaciones',
      T.MESSAGE_SENT: 'El mensaje ha sido enviado',
      T.SEND_MESSAGE: 'Enviar mensaje',
      T.MESSAGES: 'Mensajes',
      T.MESSAGES_LIST: 'Lista de mensajes',
      T.SEND: 'Enviar',
      T.ACCEPT: 'Aceptar',
      T.USER: 'Usuario',
      T.PASSWORD: 'contraseña',
      T.REPEAT_PASSWORD: 'Repetir contraseña',
      T.ABOUT_ME: 'Sobre mi',
      T.INVALID_USERNAME_OR_PASSWORD: 'Usuario o contraseña invalidos',
      T.SIGN_IN: 'Ingresar con usuario y contraseña',
      T.REGISTER: 'Registrar usuario y contraseña',
      T.BETWEEN_10_to_32_CHARACTERS: 'Debe ingresar 10 a 32 caracteres',
      T.MESSAGES: 'Mensajes',
      T.MESSAGE: 'Mensaje',
      T.MESSAGES_LIST: 'Lista de mensajes',
      T.WRITE: 'Escribe'
     }
    
def t(key):
    return es.get(key, f'bad key {key:s}') if T.lan == 'es' else key 


db = SQLAlchemy()
T.lan = 'es'
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = t(T.LOGIN_MESSAGE)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from application.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from application.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from application.main import bp as main_bp
    app.register_blueprint(main_bp)

    from application.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    if not app.debug and not app.testing:
        file_handler = RotatingFileHandler(
            Path(app.config['LOGS'], 'application.log'), 
            maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        # Check this: begin
        file_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.DEBUG)
        # Check this: end
        app.logger.info(t(T.STARTED))

    return app


from application import models
