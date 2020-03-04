#@Time    :2020/3/4 15:54
#@Author  :wuxinghui 
#@FileName: test.py
import requests

data  ={
    "head":"haha",
    "nh":"hh"
}
res = requests.post("http://127.0.0.1:5000/index",data=data)
print(res.text)