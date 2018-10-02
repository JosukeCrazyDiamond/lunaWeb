from flask import Flask, render_template, url_for,flash,redirect
from forms import RegForm, LogForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '11f915b5b49df409af92b1b8817e5a60'

posts = [
    {
        'author': 'Luna',
        'title': 'My First Title',
        'content': 'Hello World!',
        'date': 'September 30th, 2018'
    },
    {
        'author': 'Luna',
        'title': 'My Second Title',
        'content': 'Hello World Again!',
        'date': 'September 31st, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)

@app.route('/login')
def login():
    form = LogForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)