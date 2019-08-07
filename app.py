from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to the server"

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)
  
