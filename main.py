from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return redirect("/login")


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        return redirect('/secret-screen')
    return render_template('login.html')

@app.route('/secret-screen',methods=['GET','POST'])
def secretScreen():
    if request.method == 'POST':
        return redirect('/login')
    return render_template('secret-page.html')
