import re
import tkinter as tk
from urllib import parse
import tkinter.messagebox as msgbox
import webbrowser

class Vip_Parse:
# 1. 重写构造方法
    def __init__ (self, width=500, height=300):
        self.w = width
        self.h = height

        #软件名称
        self.title = "Vip视频解析助手"
        #创建软件界面
        self.root = tk.Tk(className=self.title)

        #定义播放源
        self.v = tk.IntVar()
        self.v.set(1)

        #定义用户输入视频链接
        self.url = tk.StringVar()    #指名数据类型为字符串

        #软件的上下部分
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        #控件内容设置
        #上半部分
        group = tk.Label(frame_1, text="播放通道：", padx=10,pady=10)
        tb = tk.Radiobutton(frame_1, text="通道一", variable=self.v, value=1, width=10,height=3)

        #下半部分
        label = tk.Label(frame_2, text="请输入视频地址")
        #输入框
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor="Fuchsia",highlightthickness=1, width=35)
        play = tk.Button(frame_2, text="播放", font=("楷体",12), fg="Purple", height=1, command=self.video_play)
        
        #激活控件 以及布局
        frame_1.pack()
        frame_2.pack()

        #确定位置
        group.grid(row=0,column=0)
        tb.grid(row=0,column=1)
        label.grid(row=0,column=0)
        entry.grid(row=0,column=1)
        play.grid(row=0,column=2)



    #定义播放功能
    def video_play(self):
        #视频解析网站
        port = "http://www.wmxz.wang/video.php?url="
        #判断输入的网址是否正确
       # if re.match(r"https:/[2]\w.+$", self.url.get()):
            #拿到用户输入的网址
        ip = self.url.get()
            #视频链接加密
        ip = parse.quote_plus(ip)
            #在浏览器上打开
        webbrowser.open(port + self.url.get())
        #else:
           # msgbox.showerror(title="错误", message="视频链接无效,请重新输入")

    def loop(self):
        self.root.resizable(True,True)

        self.root.mainloop()

if __name__ == '__main__':
    app = Vip_Parse()
    app.loop()