from flask import Flask, redirect, render_template, request,jsonify
import json
import jwt

app = Flask(__name__)

app.config['SECRET-KEY'] = "aosoaoasisaoos64"
with open('config.json','r') as c:
    params = json.load(c)['params']

def isLoggedIn():
    try:
        token = request.cookies.get('token')
        payload = jwt.decode(token, app.config['SECRET-KEY'],algorithms=['HS256'])
        if payload['username'] == 'Durgesh' and payload['password'] == 'Durgesh':
            print(payload)
            return True
    except Exception as e:
        return False
    return False

@app.route('/')
def home():
    return redirect("/login")


@app.route('/login',methods=['GET','POST'])
def login():
    if isLoggedIn():
        return redirect('/secret-screen')
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # print(username,password)
        if(username==params['username'] and password==params['password']):
            token = jwt.encode({
                'username':username,
                'password':password
            },key=app.config['SECRET-KEY'])
            # print(token)
            response = redirect('/secret-screen')

            response.set_cookie('token',token)
            return response
        
    return render_template('login.html')

@app.route('/secret-screen',methods=['GET','POST'])
def secretScreen():
    if(isLoggedIn()):
        return render_template('secret-page.html')
    return redirect('/login')

@app.route('/logout',methods=['POST','GET'])
def logout():
    response = redirect('/login')
    response.delete_cookie('token')
    return response
