import email
from flask import Flask, session, url_for, render_template, redirect, request, flash
from application import app, db
from application.models import Post, UserForm, UserFormUpdate, User, PostForm


'''
Teal coloured templates provided by : copyright © Design template adopted from Gurupreeth Singh: to also mention in the ackowledgements part of README.md
However I have edited them fit the purpose of the application e.g. this is why there is some jinja2 syntax in the html templates.
The bootstrap templates that inherit from a base html are made by me.
'''
@app.route("/")
def index():
	return render_template('home.html')

@app.route('/register', methods=["POST", "GET"])
def register():
	form = UserForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			#checks if email is in database and if it is not, I add the user's info in the database
			user = User.query.filter_by(email=form.email_box.data).first()
			if user is None:
				user = User(name=form.name_box.data, email=form.email_box.data)
				db.session.add(user)
				db.session.commit()
				flash(f'Thank you for joining our gluten free community {form.name_box.data}! You should recieve a confirmation email soon', 'success')
				return redirect(url_for('register')) 
			elif(len(form.email_box.data) < 3):
				flash(f'Email invalid', 'error')
				return redirect(url_for('register'))
			else:
				flash(f'Your email address has already been used. Try logging in or use a different email address', 'error')
				return redirect(url_for('register'))
	return render_template('register2.html', form = form)

@app.route("/dashboard")
def dashboard():
	list_users = User.query.all()
	return render_template('dashboard.html', list_users_in_html=list_users)


@app.route("/update/<int:id>", methods=["POST", "GET"])
def update(id):
	form = UserFormUpdate()
	if request.method == "POST":
		updated = User.query.get(id)
		updated.name = form.name_box.data
		updated.email = form.email_box.data
		if (len(updated.email) < 3):
			flash(f'Email invalid', 'error')
			return redirect(request.referrer)
		elif form.validate_on_submit():
			db.session.commit()
			flash(f'Information has been updated successfully', 'success')
			return redirect(request.referrer)
		else:
			flash(f'Email invalid', 'error')
			return redirect(request.referrer)
	return render_template('update2.html', form = form)

@app.route("/delete/<int:id>", methods=["POST", "GET"])
def delete(id):
	#checks if it's in the database first and if it is not it returns the custom 404 page
	deleted = User.query.get_or_404(id)
	db.session.delete(deleted)
	db.session.commit()
	return redirect(url_for('dashboard'))


@app.route("/addnewpost", methods=['GET', 'POST'])
def addnewpost():
	form = PostForm()
	if form.validate_on_submit():
		#query to retrieve the user
		userToFind = User.query.filter_by(name=form.author_box.data).first()
		post = Post(title=form.title_box.data, content=form.content_box.data, author=form.author_box.data, slug=form.slug_box.data, user=userToFind)
		if db.session.query(User.id).filter_by(name=post.author).first() is None:
			flash(f"You're not signed up with us! Sign up first to submit any posts", 'error')
			return redirect(request.referrer)
		else:
			db.session.add(post)
			db.session.commit()
			flash(f'Post submitted successfully!', 'success')	
			return redirect(request.referrer)
		
	return render_template('addnewpost.html', form = form)

@app.route("/posts")
def posts():
	"""
	#with error_parameter as in posts(error_parameter), displaying all posts from the database if they exist
    rows = Post.query.count()
    if rows == 0:
        return render_template('404ForNoPostsYet'), 404
    else:
        posts=Post.query.order_by(Post.date_posted)
        return render_template('posts.html', posts_for_html=posts)
	"""
	posts=Post.query.order_by(Post.date_posted)
	return render_template('posts.html', posts_for_html=posts)

@app.route("/posts/delete/<int:id>", methods=["POST", "GET"])
def deletepost(id): 
	#checks if it's in the database first and if it is not it returns the custom 404 page
	deleted = Post.query.get_or_404(id)
	try:
		db.session.delete(deleted)
		db.session.commit()
		flash(f'Post deleted successfully!', 'success')	
		posts=Post.query.order_by(Post.date_posted)
		return render_template('posts.html', posts_for_html=posts)
	except:
		flash(f'Oops! There was a problem deleting the post. Try again later', 'error')	
		posts=Post.query.order_by(Post.date_posted)
		return render_template('posts.html', posts_for_html=posts)

@app.errorhandler(404)
@app.route("/posts/<int:id>")
def apost(id):
	post=Post.query.get_or_404(id)
	return render_template('apost.html', post_for_html=post)

@app.route("/singleuser")
def singleuserprofile():
	return render_template('singleuser.html')

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/logout")
def logout():
	return render_template('home.html')

#----------------Custom error page----------------
@app.errorhandler(404)
def pageNotFound(error_parameter):
    return render_template('404.html'), 404


@app.errorhandler(500)
def serverError(error_parameter):
    return render_template('500.html'), 500