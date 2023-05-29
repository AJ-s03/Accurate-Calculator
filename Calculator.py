import tkinter as tk

win=tk.Tk()
win.geometry("225x150")
win.title("BASIC CALCULATOR")
numb1=tk.IntVar()
numb2=tk.IntVar()
tk.Entry(win,width=15,textvariable=numb1).grid(row=0,column=0)
tk.Entry(win,width=15,textvariable=numb2).grid(row=0,column=2)
def add():
     result=int(numb1.get())+int(numb2.get())
     tk.Label(win,text="=").grid(row=1,column=0)
     tk.Label(win,text=result).grid(row=1,column=2)
def minus():
     result=int(numb1.get())-int(numb2.get())
     tk.Label(win,text="=").grid(row=1,column=0)
     tk.Label(win,text=result).grid(row=1,column=2)
def Mul():
    result=int(numb1.get())*int(numb2.get())
    tk.Label(win,text="=").grid(row=1,column=0)
    tk.Label(win,text=result).grid(row=1,column=2)
def power():
     result=int(numb1.get())**int(numb2.get())
     tk.Label(win,text="=").grid(row=1,column=0)     
     if result>=100000000000000000000:
          while result>=10:
               rem=result/10
               result=rem
               count=count+1
          tk.Label(win,text=f"{result}e{count}").grid(row=1,column=1)
     else:
          tk.Label(win,text=result).grid(row=1,column=1)
def divide():
     result=int(numb1.get())/int(numb2.get())
     tk.Label(win,text="=").grid(row=1,column=0)
     tk.Label(win,text=result).grid(row=1,column=2)
def floor_divide():
     result=int(numb1.get())//int(numb2.get())
     tk.Label(win,text="=").grid(row=1,column=0)
     tk.Label(win,text=result).grid(row=1,column=2) 
def Mod():
     result=int(numb1.get())%int(numb2.get())
     tk.Label(win,text="=").grid(row=1,column=0)
     tk.Label(win,text=result).grid(row=1,column=2)
def ac():
     tk.Label(win,text="=").grid(row=1,column=0)
     tk.Label(win,text="                            ").grid(row=1,column=2)
tk.Button(win,text="AC",command=ac).grid(row=5,column=1)
tk.Button(win,text="%",width=5,command=Mod).grid(row=4,column=0)
tk.Button(win,text="//",width=5,command=floor_divide).grid(row=4,column=1)
tk.Button(win,text="/",width=5,command=divide).grid(row=3,column=1) 
tk.Button(win,text="**",width=5,command=power).grid(row=3,column=0)
tk.Button(win,text="*",width=5,command=Mul).grid(row=5,column=0)
tk.Button(win,text="-",width=5,command=minus).grid(row=2,column=1)
tk.Button(win,text="+",width=5,command=add,).grid(row=2,column=0)
tk.mainloop()
