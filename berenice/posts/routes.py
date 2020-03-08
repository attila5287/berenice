from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from berenice import db
from berenice.models import User, Post
from berenice.posts.forms import PostForm, PostDemo

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


@posts.route("/p0st/users/<int:user_1d>/delete", methods=['GET', 'POST'])
def delete_dummy_posts_from(user_1d):
    pass
    dummy_posts = Post.query.filter_by(user_id=user_1d).delete()
    db.session.commit()
    flash('Dummy posts have been deleted!', 'success')
    return redirect(url_for('main.home'))

@posts.context_processor
def inject_PostDemoList():
    pass
    PostDemoList = [
        PostDemo(title=title, content=content)
        for (title, content) in zip(
            [
                '01> welcome to python flask app!',
                '02> these are demo posts',
                '03> they only appear',
                '04> when there are no posts to show',
            ],
            [
                'A: post is a CRUD module',
                'B: create posts or delete yours',
                'C: read those created by others',
                'D: update your posts or preferences',
            ]
        )
    ]

    return dict(PostDemoList=PostDemoList)
