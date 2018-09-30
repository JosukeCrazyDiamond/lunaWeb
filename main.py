from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)