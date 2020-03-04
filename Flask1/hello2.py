#@Time    :2020/3/4 12:41
#@Author  :wuxinghui 
#@FileName: hello2.py
from flask import Flask,current_app,redirect,url_for

app = Flask(__name__)

@app.route("/")
def index():
    """定义视图函数"""
    return "hello flask"

#通过methods限定访问方式
@app.route("/post_only",methods=["POST"])
def post_only():
    return  "post only page"

@app.route("/hello",methods=["post"])
def hello():
    return "hello 1"
#只有当两者的路径和请求方式一样，上面的才会覆盖下面的
@app.route("/hello",methods=["get"])
def hello2():
    return "hello 2"

#可以设置两个路径对应一个视图函数
@app.route("/hi")
@app.route("/hi2")
def hi():
    return "hi"

@app.route("/login")
def login():
    #使用url_for的函数，通过视图函数的名字找到视图对应的url路径
    url = url_for("index")#传递一个函数名字
    #也可以直接写死  redirect("/")
    return redirect(url)


if __name__ == '__main__':
    #通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    #启动flask程序
    #app.run()
    app.run(debug=True)