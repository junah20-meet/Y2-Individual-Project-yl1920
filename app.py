from flask import *
from flask import session as login_session
from database import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/l')
def home():
	return render_template("home.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/books')
def books():
	return render_template("books.html")

@app.route('/stories',methods=['GET','POST'])
def stories():
	if request.method == 'GET' :
		return render_template('stories.html')
	else:
		Firstname = request.form['firstname']
		Lastname = request.form['lastname']
		Email = request.form['email']
		Story = request.form['message']

		add_story(Firstname, Lastname, Email, Story)
		return redirect('stories')


@app.route('/api')
def api():
	return render_template("api.html")


if __name__=='__main__':
	app.run(debug=True)