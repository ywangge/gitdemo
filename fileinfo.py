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

#保存
def save():
    try:
        f = open(filename,'w')
        content = text.get(1.0,END)
        f.write(content)
        f.close()
    except:
        #如果这是一个新建的文档保存，就用saveas指令
        saveas()
 
 #另存为
def saveas():
    f = asksaveasfilename(initialfile= '新建文档', defaultextension='.txt')
    filename = f
    window.title(os.path.basename(f))
    fw = open(f,'w')
    content = text.get(1.0,END)
    fw.write(content)
    fw.close()
    window.title(os.path.basename(f))

#引入event类来实现键盘上的复制粘贴等操作，然后用generate函数来实现

#复制 
def copy():
    text.event_generate('<<Copy>>')
#粘贴 
def paste():
    text.event_generate('<<Paste>>')

#全选 
def selectAll():
    #利用tag函数中的add操作，sel表示全选
    text.tag_add('sel','1.0',END)

#剪切
def cut():
    text.event_generate('<<Cut>>')

#撤销
def redo():
    text.event_generate('<<Redo>>')

#重做
def undo():
    text.event_generate('<<Undo>>')

#查找指定内容的个数 
def search():
    def dosearch():
        wordname = entry1.get()             #获取查找的内容--string型
        essay = str(text.get(1.0,END))#文本框的内容
        showinfo(title='查找结果：',message=("查找结果：{}共有{}个").format(wordname,essay.count(wordname)))#直接用count函数找
        
    topsearch = Toplevel(window)
    topsearch.geometry('400x50+150+200')
    label1 = Label(topsearch,text='请输入需要查找的单词')
    label1.grid(row=0, column=0,padx=5)
    entry1 = Entry(topsearch,width=20)
    entry1.grid(row=0, column=1,padx=5)
    button1 = Button(topsearch,text='查找',command=dosearch)
    button1.grid(row=0, column=3)


        