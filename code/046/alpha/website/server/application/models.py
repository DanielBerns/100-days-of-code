import base64
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import url_for, current_app
from datetime import datetime, timedelta
from application import db, login
from time import time
import json
from PIL import Image
import io
from pathlib import Path 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    last_message_read_time = db.Column(db.DateTime)
    
    posts = db.relationship('Post', 
                            foreign_keys='Post.user_id',
                            backref='author', 
                            lazy='dynamic')
    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
   
    def __repr__(self):
        return f'<User {self.username:s}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # def get_posts(self):
    #     my_posts = Post.query.filter_by(user_id=self.id)
    #     return my_posts.order_by(Post.timestamp.desc())

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            'last_seen': self.last_seen.isoformat() + 'Z',
            'post_count': self.posts.count(),
            '_links': {
                'self': url_for('api.get_user', id=self.id),
                'all_the_messages': url_for('api.all_the_messages')
            }
        }
        return data

    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1024))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.content:s}>'


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'content': self.content,
            'timestamp': self.timestamp.isoformat() + 'Z',
            'sender_id': self.sender_id,
            'recipient_id': self.recipient_id,
            'self': url_for('api.get_message', id=self.id),
        }
        return data

    def __repr__(self):
        return f'<Message({self.id:d}) {self.content:s}>'


FILESYSTEM_DEPTH = 2
FILES_PER_FOLDER = 256


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Store ({self.id:d})>'
    
    def id2FS(self):
        number = self.id
        digits = [0]*(FILESYSTEM_DEPTH + 1)
        for i in range(FILESYSTEM_DEPTH + 1):
            digits[FILESYSTEM_DEPTH - i] = number % FILES_PER_FOLDER
            number = number // FILES_PER_FOLDER
        parts = [f'{v:>03d}' for v in digits]
        name = ''.join(parts)
        folder = Path(current_app.config['PICTURES'], parts[0], parts[1])
        folder.mkdir(mode=0o700, parents=True, exist_ok=True)
        return folder, name

    @staticmethod
    def create(user):
        store = Store(user_id=user.id)
        db.session.add(store)
        db.session.commit()
        return store


ALLOWED_IMAGES = set(['png', 'jpg', 'jpeg'])


def save_image(image, store):
    try:
        current_app.logger.info('0 save_image start')
        _folder, _name = store.id2FS()
        current_app.logger.info(f'1 save_image {str(_folder):s} {_name:s}')
        image_path = Path(_folder, f'{_name:s}.png')
        current_app.logger.info(f'2 save_image {_name:s} {str(image_path):s}')
        image.save(image_path)
        current_app.logger.info(f'3 save_image {_name:s} image save')                
    except Exception as message:
        current_app.logger.error(f'4 save_image {_name:s} crash: {str(message):s}')        
        abort(500)
