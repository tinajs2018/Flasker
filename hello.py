from flask import Flask,render_template

#creating a flask instant

app= Flask(__name__)

#create a route decolorator

@app.route('/')
def index():
    first_name ='Tina'
    stuff="this < strong> text bold </strong>"
    return  render_template("index.html",first_name =first_name,stuff=stuff)
# def index():
#     return "<h1> It will be more powerful than i can imagine</h1>"

@app.route('/user/<name>')

def user(name):
    return render_template("user.html",name=name)


#creating custom error pages



#internal  server error
@app.errorhandler(500)
def page_notfound(e):
    return render_template("500.html"), 500