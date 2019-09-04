import os
def getTxt():
        txt = open("requirements.txt","r").read()#读取需要安装的第三方库
        return txt
kusTxt=getTxt()
words=kusTxt.split('\n')
for word in words:
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple "+word)#执行cmd命令
    print("{}成功安装".format(word))