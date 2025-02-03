from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Maddy Villa"

@app.route('/hello/<name>')
def hello():
    return f"hello,{name}!"
if __name__=="__main__":
     app.run(debug=True)