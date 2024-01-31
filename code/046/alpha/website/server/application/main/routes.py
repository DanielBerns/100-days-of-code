from datetime import datetime
from pathlib import Path
import os
import uuid

from flask import render_template, flash, redirect, url_for, request, current_app, jsonify, send_from_directory
from flask_login import current_user, login_required

from application import db, t, T

from application.main import bp
from application.main.forms import PostForm, MessageForm, EmptyForm
from application.models import User, Post, Message


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


def next_and_prev(posts, identifier):
    next_url = url_for(identifier, page=posts.next_num) if posts.has_next else None
    prev_url = url_for(identifier, page=posts.prev_num) if posts.has_prev else None
    return next_url, prev_url


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(content=form.content.data, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        flash(t(T.YOUR_POST_IS_LIVE_NOW))
        return redirect(url_for('main.index', page=1))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, 
        current_app.config['POSTS_PER_PAGE'], 
        False)
    
    next_url = url_for('main.index', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) if posts.has_prev else None
    
    return render_template('index.html', 
                           title=t(T.INDEX), 
                           form=form,
                           posts=posts.items, 
                           next_url=next_url,
                           prev_url=prev_url)

@bp.route('/user/followed_posts/<username>')
@login_required
def followed_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.followed_posts().paginate(
        page, 
        current_app.config['POSTS_PER_PAGE'], 
        False)
    
    next_url = url_for('main.followed_posts', 
                       username=username, 
                       page=posts.next_num) if posts.has_next else None
    prev_url = url_for('main.followed_posts', 
                       username=username, 
                       page=posts.prev_num) if posts.has_prev else None
    
    return render_template('followed_posts.html', 
                           user=user, 
                           posts=posts.items,
                           next_url=next_url, 
                           prev_url=prev_url)


@bp.route('/user/contact/<username>')
@login_required
def user_contact(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('user_contact.html', 
                           user=user, 
                           form=form)



@bp.route('/help', methods=['GET'])
def help():
    return render_template('help.html', title=t(T.HELP))


@bp.route('/user/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(t(USER_NOT_FOUND) + f' {username:s}')
            return redirect(url_for('main.index'))
        if user == current_user:
            flash(t(EACH_USER_FOLLOWS_HER_POSTS))
            return redirect(url_for('main.user_contact', username=username))
        current_user.follow(user)
        db.session.commit()
        flash(t(T.NOW_YOU_ARE_FOLLOWING_THE_POSTS_BY) + username)
        return redirect(url_for('main.user_contact', username=username))
    else:
        return redirect(url_for('main.index'))


@bp.route('/user/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(t(T.USER_NOT_FOUND) + username)
            return redirect(url_for('main.index'))
        if user == current_user:
            flash(t(T.EACH_USER_FOLLOWS_HER_POSTS))
            return redirect(url_for('main.user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash(t(T.YOU_HAVE_STOPPED_FOLLOWING_THE_POST_BY) + username)
        return redirect(url_for('main.user_contact', username=username))
    else:
        return redirect(url_for('main.index'))


@bp.route('/all_the_posts')
@login_required
def all_the_posts():
   page = request.args.get('page', 1, type=int)
   posts = Post.query.order_by(Post.timestamp.desc()).paginate(
       page, current_app.config['POSTS_PER_PAGE'], False)
   next_url = url_for('main.all_the_posts', page=posts.next_num) \
       if posts.has_next else None
   prev_url = url_for('main.all_the_posts', page=posts.prev_num) \
       if posts.has_prev else None
   return render_template("all_the_posts.html", 
                          title=t(T.ALL_THE_POSTS), 
                          posts=posts.items,
                          next_url=next_url, 
                          prev_url=prev_url)


@bp.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = User.query.filter_by(username=recipient).first_or_404()
    form = MessageForm()
    if form.validate_on_submit():
        a_message = Message(author=current_user, 
                      recipient=user,
                      content=form.message.data)
        db.session.add(a_message)
        db.session.commit()
        flash(t(T.MESSAGE_SENT))
        return redirect(url_for('main.followed_posts', username=recipient))
    return render_template('send_message.html', 
                           title=t(T.SEND_MESSAGE),
                           form=form, 
                           recipient=recipient)

@bp.route('/messages')
@login_required
def messages():
    current_user.last_message_read_time = datetime.utcnow()
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    messages = current_user.messages_received.order_by(
        Message.timestamp.desc()).paginate(
            page, 
            current_app.config['POSTS_PER_PAGE'], 
            False)
    next_url = url_for('main.messages', page=messages.next_num) \
        if messages.has_next else None
    prev_url = url_for('main.messages', page=messages.prev_num) \
        if messages.has_prev else None
    return render_template('messages.html', 
                           title=t(T.MESSAGES),
                           nav_h1=t(T.MESSAGES_LIST),
                           messages=messages.items,
                           next_url=next_url, 
                           prev_url=prev_url)
