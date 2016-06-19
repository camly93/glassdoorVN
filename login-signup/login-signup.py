from flask import Flask,render_template,request, redirect,url_for,make_response
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
app = Flask(__name__)
#home page
@app.route('/')
def home():
    return "Welcome home!"
@app.route('/login', methods=['POST', 'GET'])
def login():
<<<<<<< HEAD
    error = None
    if request.method == 'POST':
        if request.form['userid']=='aaaa':
            print('x')
        else:
            error = 'Invalid username/password'
        a=(request.args.get('h1',''))
        print(a)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
@app.route('/signup')
def index():
    resp = make_response(render_template('xxx.html'))
    # resp.set_cookie('username', 'the username')
    return resp
@app.route('/search-result',methods=['POST','GET'])
def search(a=pagelist[0],current=1,c=len(pagelist)):
    if request.method=='POST':
        current=int(request.form['gotopage'])
        a=pagelist[current-1]
        return render_template('xxx.html', everything=a, manypage=c, current=current)
    return render_template('xxx.html',everything=a,manypage=c,current=current)
=======
    return render_template('login.html')

@app.route('/review')
def review():
    return render_template('input-review.html')


>>>>>>> 78997c1dd575a0e7fcfa83272a4e115067da4f4f
if __name__ == '__main__':
    app.run()
