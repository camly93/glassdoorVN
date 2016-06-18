from flask import Flask,render_template

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/review')
def review():
    return render_template('input-review.html')


if __name__ == '__main__':
    app.run()
