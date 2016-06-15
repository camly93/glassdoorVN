from flask import Flask,render_template,request, redirect

app = Flask(__name__, static_url_path ='/static')

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print("someone is logging...")
        return redirect('/')
    return render_template('Home.html')

@app.route('/about-us')
def aboutus():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
