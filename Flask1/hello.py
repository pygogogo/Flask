from flask import Flask

# 创建flask对象
#模块名。flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，tempaltes为模板目录
app = Flask(__name__,
static_url_path="/python", #访问静态资源的url前缀
static_folder="static",#以当前目录下的static为静态目录
template_folder="templates")  #导入路径，寻找静态目录与模板目录位置的参数，当你传的文件名字Flask没有找到的话，就会默认当前文件为启动文件，
#如果传的是其他文件，如果能找到的话，就会是那个文件所在的目录为根目录
#当你在static中创建一个index.html时，当你访问http://127.0.0.1:5000/static/index.html，浏览器会顺着路径自己去访问这个index文件，其中的static是static_url_path设置的路径

#配置参数的使用方式
#1.使用配置文件
#app.config.from_pyfile("config.cfg")
#2.使用对象配置参数
class Config1(object):
    DEBUG = True
    IT = "python"  #必须要大写
app.config.from_object(Config1)
#3.直接操作config的字典对象
# app.config["DEBUG"]=True


@app.route("/")
def index():
    """定义的视图函数"""
    #1.直接从全局对象app的config字典中取值

    print(app.config.get("IT"))  #在视图函数中读取配置参数
    # print(current_app.config.get("iicast"))
    return "hello flask"

if __name__ == '__main__':
    #启动flask程序
    #app.run(host="192.168.199.147",port=5000)
    app.run(host="0.0.0.0", port=5000,debug=True)#通配符只要是代表当前主机的ip地址，都可以
