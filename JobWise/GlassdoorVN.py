from flask import Flask,render_template,request, redirect

app = Flask(__name__, static_url_path ='/static')

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print("someone is searching...")
        return redirect('/home')
    return render_template('Login.html')

@app.route('/about-us')
def aboutus():
    return render_template('About-us.html')

@app.route('/home', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print("someone is searching...")
        return redirect('/company')
    return render_template('Home.html')

@app.route('/company-review')
def signup():
    return render_template('Company-review.html')

# @app.route('/review-form')
# def review_form():
#     return render_template('Form-review.html')

@app.route('/review-form')
def review_form2():
    return render_template('Form-review2.html')

if __name__ == '__main__':
    app.run()
