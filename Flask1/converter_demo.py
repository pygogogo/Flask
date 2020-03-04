#@Time    :2020/3/4 13:37
#@Author  :wuxinghui 
#@FileName: converter_demo.py
from flask import Flask,current_app,redirect,url_for
from werkzeug.routing import BaseConverter
app = Flask(__name__)

@app.route("/")
def index():
    """定义视图函数"""
    return "hello flask"

#转换器的种类
#int   接受整数
#float  接受浮点数
#path   和默认的相似，但也接受斜线
#127.0.0.1:5000/goods/123
#@app.route("/goods/<int:goods_id>")
@app.route("/goods/<goods_id>")#不加转换器类型的话，默认为普通的字符串规则（除了/的字符）
def goods_detail(goods_id):
    """定义的视图函数"""
    return "goods detail page %s" %goods_id



#1.定义自己的转换器
class MobileConverter(BaseConverter):
    def __init__(self,url_map):
        super().__init__(url_map)
        self.regex = r"1[34578]\d{9}"



class RegexConverter(BaseConverter):
    def __init__(self,url_map,regex):
        #调用父类的初始化方法
        super().__init__(url_map)
        #将正则表达式的参数保存到对象属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex
    def to_python(self, value):
        #value是在路径进行正则表达式匹配的时候提取的参数
        return value

    def to_url(self, value):
        """使用url_for的时候被调用"""
        return value


#2.将自定义的转换器添加到flask应用中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters["mobile"] = MobileConverter
#3.自定义转换器的使用

#@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
@app.route("/send/<mobile:mobile_number>")
def send_sms(mobile_number):
    return "send sms to %s"%mobile_number

@app.route("/head")
def head():
    url = url_for("send_sms",mobile_number="18632222222")#mobile_number就是send_sms中的命名一样。先传递给to_url,然后to_url的返回值再传递给  /send/value当作url_for的返回值
    return redirect(url)

if __name__ == '__main__':
    #通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    #启动flask程序
    #app.run()
    app.run(debug=True)