from flask import Flask,render_template,request, redirect
import pymongo
db_url = "mongodb://Raventine:raven123@ds013564.mlab.com:13564/job-offer"
db = pymongo.MongoClient(db_url).get_default_database()
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

@app.route('/review-form', methods=['POST','GET'])
def review_form2():
    collection=db['company-review']
    if request.method == 'POST':
        collection.insert_one({'Cong ty': request.form['data_1'],'Xep hang': request.form['data_2'],'Tieu de': request.form['data_3'],'Diem cong': request.form['data_4'],'Diem tru': request.form['data_5'],'Trai nghiem': request.form['data_6'],'Gop y': request.form['data_7']})
    return render_template('Form-review2.html')

if __name__ == '__main__':
    app.run()
