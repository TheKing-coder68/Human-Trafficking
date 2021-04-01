from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route("/",methods=['GET','POST'])
def home():
   return render_template("index.html")

@app.route("/about",methods=['GET','POST'])
def about():
   return render_template("about.html")

@app.route("/sources",methods=['GET','POST'])
def sources():
   return render_template("source.html")

app.run(host='0.0.0.0', port=8080)