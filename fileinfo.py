import os
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from PIL import Image,ImageTk

#打开文件 
def openfile():  
    global filename
    #利用tf库里的askopenfilename函数得到文件的绝对路径。如果不是很清晰，后面用defaultextension函数添加'txt'来说明文件类型
    filename = askopenfilename(defaultextension = '.txt')
    if filename == '':
        filename=None
    else:
        ##利用os.path.basename()函数返回path最后的文件名，即格式
        window.title(os.path.basename(filename))
        #清空原来的文档
        text.delete(1.0,END)
        f = open(filename,'r')
        #读入新的文档
        text.insert(1.0,f.read())
        f.close()
#新建文档
def new():
    window.title('新建文档')
    filename = None
    text.delete(1.0,END)

        