#
# An app that allows the analysis of employee skills
#
# copyright IBM 2017
#
# App alos uses functions in the functions/ dir, i think the functions are self explanatory, but let me know if you have any questions


import os, json
import pandas as pd
from functions.auth_user import auth, checkID
from functions.database import getAllUsers
from functions.auth_watson import getConversationSevice, WORKSPACE
from functools import reduce
from flask import Flask, jsonify, request, Response, flash, \
                    redirect, render_template, url_for, abort
from flask_login import LoginManager, UserMixin,\
                                login_required, login_user, logout_user

app = Flask(__name__)

app.config.update(SECRET_KEY = 'aoun@ibm')

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# user model
class User(UserMixin):

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

# to clear cache after some time to ensure js and images are updated during dev
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


# api to query the db, takes in a json object that contains 6 key-val pairs, each val is a list of skills,
# markts, specialiyt, primary industry, secondary industry, and primary skills.


@app.route('/query' , methods=['GET'])
@login_required
def getPeople():

    data = getAllUsers()
    columns = data.columns.values

    query = json.loads(request.args.get('query'))

    s = json.loads(query['skills'])
    m = json.loads(query['market'])
    sp = json.loads(query['speciality'])
    pi = json.loads(query['pindustry'])
    si = json.loads(query['sindustry'])
    ps = json.loads(query['pskills'])

    print query

    sResult = []
    mResults = []
    spResults = []
    piResults = []
    siResults = []
    psResults = []
    d = []
    
    # obtain records that match each query list
    if len(s) > 0:
        sResult = set(data.loc[data['skills'].isin(s)].index.values)
        d.append(sResult)

    if len(m) > 0:
        mResults = set(data.loc[data['Market'].isin(m)].index.values)
        d.append(mResults)

    if len(sp) > 0:
        spResults = set(data.loc[data['Specialty'].isin(sp)].index.values)
        d.append(spResults)

    if len(pi) > 0:
        piResults = set(data.loc[data['Primary Industry'].isin(pi)].index.values)
        d.append(piResults)

    if len(si) > 0:
        siResults = set(data.loc[data['Secondary Industry'].isin(si)].index.values)
        d.append(siResults)

    if len(ps) > 0:
        psResults = set(data.loc[data['Primary Skill'].isin(si)].index.values)
        d.append(psResults)

    # find the intersection between matched records
    r = list(reduce(set.intersection, d) )
    d = data.loc[r]
    result = d.to_json(orient='records')

    return result

# route to render chat ui
@app.route('/chat')
@login_required
def chat():

    return render_template('chat.html')

# route that recieves a message and sends it to watson  conversation and gets back a response.
# if response is query, it then checks for entities and then should pass these to the query api
# (not yet implimented). if not, it just returns the response from watson conversation

@app.route('/message')
@login_required
def message():

    query = request.args.get('message')
    m = {'text': query}
    conversation = getConversationSevice()
    response = conversation.message(WORKSPACE, m)
    entities = json.dumps(response['entities'])
    e = []
    for ent in entities:
        print ent
        # e.append(ent['value'])
    print e
    res = json.dumps(response['output']['text'][0])
    return res

# render home page
@app.route('/')
@login_required
def home():
    return render_template('index.html')


# get = renders home page
# put = authenticates
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        success, uid = auth(username, password)
        if(success):
            login_user(User(uid, username, password))
            flash('Logged in successfully.')
            return redirect(url_for('home'))
        else:
            return abort(401)
    else:
        return render_template("login.html")

# api for login
@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return url_for('login')

# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed, Invalid username or password</p>')

# callback to reload the user object
@login_manager.user_loader
def load_user(uid):
    user = checkID(uid)
    return User(user['id'], user['name'], user['password'])

port = os.getenv('PORT', '8080')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port), debug=True)
