from flask import Flask,render_template, request #calling the flask library

app = Flask(__name__) #Instantiating the app

@app.route("/")  #route, links this goes to the homepage
def home():
    return render_template('homepage.html')


@app.route("/contact")  #route, links this goes to the homepage
def contact():
    return render_template("contact.html")

@app.route("/signup")  #route, links this goes to the homepage
def signup():
    return render_template("signup.html")

@app.route("/confirmation")  #route, links this goes to the homepage
def Confirmation():
    First=request.args.get('First')
    Last=request.args.get('Last')
    return render_template("confirmation.html", First=First, Last=Last)

@app.errorhandler(404)
def Error(e):
    return render_template('404.html'), 404


if __name__== "__main__":
    app.run(debug=True) 