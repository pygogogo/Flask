from flask import Flask,request



app = Flask(__name__)


@app.route("/upload",methods=["POST"])
def upload():
    """接收前端传送过来的文件"""
    file_obj = request.files.get("pic")
    if file_obj is None:
        #表示没有发送文件
        return "未上传文件"
    #将文件保存到本地
    #1.创建一个文件
    f = open("./demo.jpg","wb")
    data = file_obj.read()
    f.write(data)
    f.close()
    return "上传成功"
if __name__ == '__main__':
    app.run(debug=True)