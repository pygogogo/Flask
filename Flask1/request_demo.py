#@Time    :2020/3/4 15:51
#@Author  :wuxinghui 
#@FileName: request_demo.py

#coding:utf-8

from flask import Flask,request

app = Flask(__name__)

@app.route("/index",methods=["GET","POST"])
def index():
    #request中包含了前端发送过来的所有请求数据
    #通过form和data是用来提取请求体中数据
    #通过request.form可以直接提取请求体中的表单格式的数据，是一个类字典的对象
    #通过get方法可以拿到多个同名参数的第一个
    name = request.form.get("name")
    age = request.form.get("age")
    name_li = request.form.getlist("name")
    #如果是请求体而数据不是表单格式的(如json格式)，可以通过request.data获取
    print(request.data)
    #args是用来提取url中的参数（查询字符串）
    city = request.args.get("city")
    
    return "name=%s,age=%s"%(name,age)



if __name__ == '__main__':
    app.run(debug=True)