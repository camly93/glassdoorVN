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
for x in everything:
    litt.append(x)
print(len(litt)//100+1)
for x in range (len(litt)//100+1):
    temp = []
    if cur<(len(litt)//100):
        for y in range(100):
            temp.append(litt[x*100+y])
        cur=cur+1
    else:
        for y in range(len(litt)-(len(litt)//100)*100):
            temp.append(litt[x*100+y])
    pagelist.append(temp)
app = Flask(__name__)
#home page
@app.route('/')
def home():
    return "Welcome home!"
@app.route('/login', methods=['POST', 'GET'])
def login():
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
if __name__ == '__main__':
    app.run()
