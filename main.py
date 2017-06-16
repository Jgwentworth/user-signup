from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_index():
    return render_template("index.html")    

def is_blank(resp):
    if len(resp) == 0:
        return True
    else:
        return False

def is_valid(resp):
    if " " in resp:
        return False
    elif (len(resp) < 3) or (len(resp) > 20):
        return False
    else:
        return True                   

@app.route("/", methods=["POST"],)
def validate_response():

    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    name_error = ''
    pass_error = ''
    pass_error2 = ''
    email_error = ''

    if is_blank(username):
        name_error = "Empty field"
    else:    
        if not is_valid(username):
            name_error = "Not valid (Between 3-20 characters and no whitespace."
            username = ""
    if is_blank(password):
        pass_error = "Empty field"
    else:
        if not is_valid(password):
            pass_error = "Not valid (Between 3-20 characters and no whitespace."
            password =""
    if is_blank(password2):
        pass_error2 ="Empty field"
    else:
        if not is_valid(password2):
            pass_error2 = "Not valid (Between 3-20 characters and no whitespace."
            password2 = ""      
        elif password != password2:
            pass_error2 = "Not valid (Not matching)"
            password2 = ""
    if not name_error and not pass_error and not pass_error2:
        name = username
        return redirect("/welcome?name={0}".format(name))        
    else:
        return render_template("index.html",
            name_error = name_error,
            pass_error = pass_error,
            pass_error2 = pass_error2,
            email_error = email_error
    )        
@app.route("/welcome")
def welcome():
    name = request.args.get('name')
    return "<h1>Welcome {0}!</h1>".format(name)    

app.run()        