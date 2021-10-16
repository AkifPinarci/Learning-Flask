from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('index.html', content=["Mehmet", "Akif", "Pinarci"], r=2)

@app.route('/about')
def about():
    return "This is about page"

@app.route('/input')
def login():
    return f"Hello"

@app.route('/admin')
def admin():
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run()


