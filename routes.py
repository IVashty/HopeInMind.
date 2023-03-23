from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/category')
def category():
    return render_template('category.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
