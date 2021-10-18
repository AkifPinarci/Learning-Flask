# Useful notes
# Learn more about Jinja templates


from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url')
def admin():
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)