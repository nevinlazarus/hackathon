from app import app
from flask import render_template

@app.route("/") #route decorators to create mappings from urls to this function
@app.route("/index") #this is hat you put in the url to call the function 
def index():
    user = {"nickname" : "dennis"}
    return render_template("index.html", title = "home", user = user)

@app.route("/m8")
def mate():
    return "u wot m8"
