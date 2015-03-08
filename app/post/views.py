from . import post
from .forms import PostForm
from .models import Post
from ..auth.models import Permission#, User
from flask import render_template, redirect, url_for
from .. import db#, login_manager
from flask.ext.login import login_user, login_required, current_user

@post.route('/posts', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    #"""
    #if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
    if form.validate_on_submit():
        post = Post(body=form.body.data)#, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    #"""
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('posts/index.html', form=form, posts=posts)
    #return render_template('posts/index.html')

@post.route('/posts/<int:id>')
@login_required
def post(id):
    post = Post.query.get_or_404(id)
    #return render_template('posts/index.html', form=form, posts=posts)
    return "<h1>Hello POSTS</h1>"
