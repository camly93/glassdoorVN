from flask import Flask,render_template,request, redirect
import pymongo
db_url = "mongodb://Raventine:raven123@ds013564.mlab.com:13564/job-offer"
db = pymongo.MongoClient(db_url).get_default_database()

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

app = Flask(__name__, static_url_path ='/static')

#trang LOG IN
@app.route('/', methods=['POST', 'GET'])
def login():
    collection = db['account']
    account = collection.find()
    if request.method == 'POST':
        for x in account:
            if request.form['username']==x['username'] and x['password']==request.form['password']:
                return redirect('/home')
    return render_template('Login.html')

#trang ABOUT US
@app.route('/about-us')
def aboutus():
    return render_template('About-us.html')

#trang SEARCH
@app.route('/home', methods=['GET','POST'])
def home():
    temp=[]
    collection = db['job-offer']
    everything = collection.find()
    if request.method == 'POST':
        for x in everything:
            print(x['location'])
            if x['location']==request.form['CITY']:
                temp.append(x)
        print(temp)
        return render_template('Company-list.html',everything=temp, manypage=len(temp)//25, current=1)
    return render_template('Home.html')

#trang COMPANY REVIEW
@app.route('/<company>-review',methods=['POST','GET'])
def signup(company,noidung='',info=''):
    collection=db['job-offer']
    f=collection.find()
    for x in f:
        if x['company']==company:
            info=x['company-info']
    collection=db['company-review']
    y=collection.find()
    temp=[]
    if request.method=='POST':
        a=request.form['data_2']
        collection.insert_one({'company':company,
                               'noidung':a})
    for x in y:
        if x['company']==company:
            temp.append(x['noidung'])
    return render_template('Company-review.html',company=company,info=info,noidung=temp)

@app.route('/company-review', methods=['GET','POST'])
def search2():
    temp=[]
    collection = db['job-offer']
    everything = collection.find()
    if request.method == 'POST':
        for x in everything:
            print(x['location'])
            if x['location']==request.form['CITY']:
                temp.append(x)
        print(temp)
        return render_template('Company-list.html', everything=temp, manypage=len(temp)//25, current=1)
    return render_template('Company-review.html')

#trang COMPANY LIST
@app.route('/company-list',methods=['POST','GET'])
def search(a=pagelist[0],current=1,c=len(pagelist)):
    if request.method=='POST':
        current=int(request.form['gotopage'])
        a=pagelist[current-1]
        return render_template('Company-list.html', everything=a, manypage=c, current=current)
    return render_template('Company-list.html',everything=a,manypage=c,current=current)
    # return render_template('Login.html')

if __name__ == '__main__':
    app.run()
