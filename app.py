<<<<<<< HEAD
from flask import Flask,render_template,request, redirect
import pymongo
db_url = "mongodb://Raventine:raven123@ds013564.mlab.com:13564/job-offer"
db = pymongo.MongoClient(db_url).get_default_database()
=======
from pymongo import MongoClient
client = MongoClient('mongodb://Raventine:raven123@ds013564.mlab.com:13564/job-offer')
db=client['job-offer']
collection=db['job-offer']
everything=collection.find()
litt=[]
pagelist=[]
temp=[]
cur=0
a=25
for x in everything:
    litt.append(x)
print(len(litt)//a+1)
for x in range (len(litt)//a+1):
    temp = []
    if cur<(len(litt)//a):
        for y in range(a):
            temp.append(litt[x*a+y])
        cur=cur+1
    else:
        for y in range(len(litt)-(len(litt)//a)*a):
            temp.append(litt[x*a+y])
    pagelist.append(temp)

from flask import Flask,render_template,request, redirect,url_for,make_response

>>>>>>> fed92c35a4e44c98dff5ec8f0f50f0bc2c261cf7
app = Flask(__name__, static_url_path ='/static')

#trang LOG IN
@app.route('/', methods=['POST', 'GET'])
def login():
    collection = db['account']
    account = collection.find()
    if request.method == 'POST':
        for x in account:
            if request.form['username']==x['username'] and x['password']==request.form['password']:
                return redirect('/Home.html')
    return render_template('Login.html')

#trang ABOUT US
@app.route('/about-us')
def aboutus():
    return render_template('About-us.html')

#trang SEARCH
@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print("someone is searching...")
        return redirect('/company')
    return render_template('Home.html')

#trang COMPANY REVIEW
@app.route('/company-review')
def signup():
    return render_template('Company-review.html')

<<<<<<< HEAD
# @app.route('/review-form')
# def review_form():
#     return render_template('Form-review.html')

@app.route('/review-form', methods=['POST','GET'])
def review_form2():
    collection=db['company-review']
    if request.method == 'POST':
        collection.insert_one({'Cong ty': request.form['data_1'],'Xep hang': request.form['data_2'],'Tieu de': request.form['data_3'],'Diem cong': request.form['data_4'],'Diem tru': request.form['data_5'],'Trai nghiem': request.form['data_6'],'Gop y': request.form['data_7']})
    return render_template('Form-review2.html')
=======
#trang REVIEW FORM
@app.route('/review-form')
def review_form2():
    return render_template('Form-review.html')

#trang COMPANY LIST
@app.route('/company-list',methods=['POST','GET'])
def search(a=pagelist[0],current=1,c=len(pagelist)):
    if request.method=='POST':
        current=int(request.form['gotopage'])
        a=pagelist[current-1]
        return render_template('Company-list.html', everything=a, manypage=c, current=current)
    return render_template('Company-list.html',everything=a,manypage=c,current=current)
    # return render_template('Login.html')
>>>>>>> fed92c35a4e44c98dff5ec8f0f50f0bc2c261cf7

if __name__ == '__main__':
    app.run()
