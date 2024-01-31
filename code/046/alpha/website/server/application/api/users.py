from flask import jsonify, request, url_for, abort, current_app
from application import db, t, T
from application.models import User, Post, Message, Store, save_image
from application.api import bp
from application.api.auth import token_auth
from application.api.errors import bad_request

from datetime import datetime


@bp.route('/users/current', methods=['GET'])
@token_auth.login_required
def get_current_user():
    current_user = token_auth.current_user()
    return jsonify(current_user.to_dict())


@bp.route('/users/all', methods=['GET'])
@token_auth.login_required
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    if token_auth.current_user().id != id:
        abort(403)
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    if 'username' in data and data['username'] != user.username and \
            User.query.filter_by(username=data['username']).first():
        return bad_request(t(DIFFERENT_USERNAME))
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())


@bp.route('/users/followers/<int:id>', methods=['GET'])
@token_auth.login_required
def get_followers(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followers, page, per_page, 'api.get_followers', id=id)
    return jsonify(data)


@bp.route('/users/followed/<int:id>', methods=['GET'])
@token_auth.login_required
def get_followed(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followed, page, per_page, 'api.get_followed', id=id)
    return jsonify(data)


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if 'username' not in data or 'password' not in data:
        return bad_request(NO_USER_CREDENTIALS)
    if User.query.filter_by(username=data['username']).first():
        return bad_request(t(DIFFERENT_USERNAME))
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@bp.route('/messages/all', methods=['GET'])
@token_auth.login_required
def all_the_messages():
    current_user = token_auth.current_user()
    current_user.last_message_read_time = datetime.utcnow()
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    messages = current_user.messages_received.order_by(Message.timestamp.desc())
    data = Message.to_collection_dict(messages, page, per_page, 'api.all_the_messages')
    return jsonify(data)


@bp.route('/messages/empty', methods=['GET'])
@token_auth.login_required
def delete_all_the_messages():
    user = User.query.filter_by(username='charliebot').first_or_404()
    current_user = token_auth.current_user()
    if user == current_user:    
        current_user.last_message_read_time = datetime.utcnow()
        db.session.commit()
        messages = current_user.messages_received.order_by(Message.timestamp.desc())
        if messages:
            for m in messages:
                db.session.delete(m)
            db.session.commit()
        data = {'result': 'queue is empty'}
    else:
        data = {'result': 'invalid request'}
    return jsonify(data)


@bp.route('/messages/<int:id>', methods=['GET'])
@token_auth.login_required
def get_message(id):
    message = Message.query.get_or_404(id)
    current_user = token_auth.current_user()
    if message.sender_id == current_user.id:
        return jsonify(message.to_dict())
    elif message.recipient_id == current_user.id:
        return jsonify(message.to_dict())
    else:
        return bad_request("current user can not request this message")
    
@bp.route('/posts', methods=['POST'])
@token_auth.login_required
def publish_post():
    current_user = token_auth.current_user()
    data = request.get_json() or {}
    try:
        content = data['content']
    except KeyError:
        content = '\n'.join([f'{str(k):s}: {str(v)}' for k, v in data.items()])
    new_post = Post(content=content, author=current_user)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(current_user.to_dict())
