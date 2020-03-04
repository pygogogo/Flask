#@Time    :2020/3/4 15:51
#@Author  :wuxinghui 
#@FileName: request_demo.py

#coding:utf-8

from flask import Flask,request

app = Flask(__name__)

@app.route("/index",methods=["GET","POST"])
def index():
    print(request.headers)
    print(request.form)
    return "hello world"



if __name__ == '__main__':
    app.run(debug=True)