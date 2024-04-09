from flask import Flask, render_template, redirect


app=Flask(__name__)


#1. Home landing page
@app.route("/")
def index_page(): #returns only mere text

    
    return render_template("template.html")


#2. About us page
#this route /path will return a html page from templates folder
@app.route("/about-us")
def about_page1():

    #more business here
    return render_template("about.html")

#3. Contact us page:

@app.route("/contact-us")
def page_ya_contacts():
    #andika chochote hapa
    return render_template("contacts.html")


#4. App ya tool page:

@app.route("/tool", methods=["POST","GET"])
def app_ya_tool():
    #andika chochote hapa
    return render_template("tool.html")

if __name__=="__main__":
    app.run(port="2020",debug=True)


