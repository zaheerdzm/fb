from flask import Flask, render_template,request,redirect,flash,url_for,json

app = Flask(__name__)
@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':

    app.run(debug=True)
