# from tkinter import*
# window=Tk()
# window.geometry("200x200")
# NameLabel=Label(window,text="welcome to tkinder")
# NameLabel.pack()
# NameEntry=Entry(window)
# NameEntry.pack()
# def getname():
#     name=NameEntry.get()
#     print(name)
# submitButton=Button(window,text="submit",command=getname)
# submitButton.pack()
# result=Label(window,text="")
# window.mainloop()    
# from tkinter import*
# window=Tk()
# window.geometry("150x150")
# Namelabel=Label(window,text="enter the number",bg="blue",fg="green",font=30)
# Namelabel.pack()
# numberentry=Entry(window,font=30)
# numberentry.pack()
# def getnumber():
#     number=numberentry.get()
#     if int(number)%2==0:
#         resultLabel=Label(window,text="the number is even")
#         resultLabel.pack()
#     else:
#         resultLabel=Label(window,text="the number is odd")
#         resultLabel.pack()    
# submitbutton=Button(window,text="submit",command=getnumber)
# submitbutton.pack()
# window.mainloop()
# from tkinter import*
# window=Tk()
# window.geometry("300x300")
# namelabel=Label(window,text="enter the number",bg="yellow",fg="green",font=25)
# namelabel.pack()
# numberentry=Entry(window,font=25)
# numberentry.pack()
# def getnumber():
#     number=int(numberentry.get())
#     temp=number
#     rev=0
#     while number>0:
#         last_digit=number%10
#         rev=(rev*10)+last_digit
#         number=number//10
#     if temp==rev:
#         resultlabel=Label(window,text="the number is palindrome")
#         resultlabel.pack()
#     else:
#         resultlabel=Label(window,text="the number is not palindrome")
# submitbutton=Button(window,text="submit",command=getnumber)
# submitbutton.pack()
# window,mainloop()                
                    
#grid
# from tkinter import*
# window=Tk()
# NameEntry=Entry(window,font=24)
# NameEntry.pack()
# def getname():
#     name=NameEntry.get()
#     print(name)   
# ButtonOne=Button(window,text="ButtonOne",padx=10,pady=10)
# ButtonOne.grid(row=0,column=0,padx=20,pady=20)
# ButtonTwo=Button(window,text="button Two",padx=10,pady=10)
# ButtonTwo.grid(row=0,column=1)
# ButtonThree=Button(window,text="Button Three",padx=10,pady=10)
# ButtonThree.grid(row=1,column=0,columnspan=2,sticky="ew")
# window.mainloop()
# from tkinter import*
# window=Tk()
# Labelone=Label(window,text="hello")
# Labelone.pack()
# NameEntry= Entry(window,font=20)
# NameEntry.pack()
# def getname():
#     name=NameEntry.get()
#     print(name)
# SubmitButton=Button(window,text="SUBMIT",command=getname)   
# SubmitButton.pack() 

# window.mainloop() 
# from tkinter import*
# window=Tk()
# Name=Label(window,text="Gender")
# Name.pack()
# m=IntVar
# male=Checkbutton(window,text="MALE",variable=m)
# male.pack()
# f=IntVar
# female=Checkbutton(window,text="FEMALE",vaariable=f)
# female.pack()
# def getgender():
#     gender.
# from tkinter import*
# window=Tk()
# expression=StringVar()
# def handleclick(value):
#     old_exp=expression.get()
#     new_exp=old_exp+value
#     expression.set(new_exp)  
# input=Entry(window,textvariable=expression)
# input.pack()
# ButtonOne=Button(window,text="1",command=lambda:handleclick("1"))
# ButtonOne.pack()

# ButtonOne=Button(window,text="2",command=lambda:handleclick("2"))
# ButtonOne.pack()
# ButtonOne=Button(window,text="3",command=lambda:handleclick("3"))
# ButtonOne.pack()
# ButtonOne=Button(window,text="4",command=lambda:handleclick("4"))
# ButtonOne.pack()
# btn=Button(window,text="SHOW",command=handleclick)
# btn.pack()
# window.mainloop()
# import tkinter as tk
# root=tk.Tk()
# root.grid("HELLO")
# label1=tk.Label(root,text="Label 1",bg="lightblue")

# label2=tk.Label(root,text="Label 2",bg="lightred")
# label3=tk.Label(root,text="Label 3",bg="lightgreen")
# label4=tk.Label(root,text="Label 4",bg="lightgrey")

# label1.grid(row=0,column=0,padx=10,pady=10)
# label2.grid(row=0,column=1,padx=10,pady=10)
# label3.grid(row=1,column=0,padx=10,pady=10)
# label4.grid(row=1,column=1,padx=10,pady=10)
# root.mainloop()
# from tkinter import*
# window=Tk()
# res=eval("2+3")
# print(res)
# from tkinter import*
# window=Tk()
# def button_click(value):
#     current=Entry.get()
#     Entry.delete(0,Tk.END)
#     Entry.insert(Tk.END,(current+value))
# def evaluate():
#     try:
#         result=eval(Entry.get())
#         Entry.delete(0,Tk.END)
#         Entry.insert(Tk.END,result)
#     except Exception as e:
#         Entry.delete(0,Tk.END)
#         Entry.insert(Tk.END,"Error")

# def clear():
#     Entry.delete(0,Tk.END)

# root=Tk.Tk()
# root.title("CALCULATOR")

# input=Entry
# from tkinter import*
# window=Tk()
# expression=StringVar()
# def handleclick(value):
#     oldexp=expression.get()
#     newexp=oldexp+value
#     expression.set(newexp)
# input=Entry(window,textvariable=expression)
# input.grid(ColumnSpan=4)
# buttonseven=Button(window,textvariable="7",padx=10,pady=10,command=lambda:handleclick("7"))  
# buttonseven.pack()
# buttonsix=Button(window,textvariable="6",padx=10,pady=10,command=lambda:handleclick("6"))  
# buttonsix.pack()
# buttonfive=Button(window,textvariable="5",padx=10,pady=10,command=lambda:handleclick("5"))  
# buttonfive.pack()
# buttonfour=Button(window,textvariable="4",padx=10,pady=10,command=lambda:handleclick("4"))  
# buttonfour.pack()
# buttonthree=Button(window,textvariable="3",padx=10,pady=10,coomand=lambda:handleclick("3"))  
# buttonthree.pack()
# buttontwo=Button(window,textvariable="2",padx=10,pady=10,coomand=lambda:handleclick("2"))  
# buttontwo.pack()
# buttonone=Button(window,textvariable="1",padx=10,pady=10,coomand=lambda:handleclick("1"))  
# buttonone.pack()
# # window.mainloop()
# from tkinter import*
# window=Tk()
# window.title("CALCULATOR")


# def handleClick(value):
#     value_from_expression=expression.get()
#     value_from_expression=value_from_expression+value
#     expression.set(value_from_expression)
# expression=StringVar()

# def result():
#     value=input.get()
#     c=eval(value)
#     input.delete(0,END)
#     input.insert(END,c)
# def clearALL():
#     input.delete(END,0)
# def undo():
#     value=input.get()
#     input.delete(len(value)-1) 
# def Zero():
#     value=input.get()
#     if len(value)==1:
#         input.delete(0,END)
#     input.insert(END,0)  

# input=Entry(window,font=24,textvariable=expression)
# input.grid(row=0,column=0,columnspan=4,sticky="ew")


# buttonseven=Button(window,text="7",padx=20,pady=20,command=lambda:handleClick("7"))
# buttonseven.grid(row=1,column=0)

# buttoneight=Button(window,text="8",padx=20,pady=20,command=lambda:handleClick("8"))
# buttoneight.grid(row=1,column=1)

# buttonnine=Button(window,text="9",padx=20,pady=20,command=lambda:handleClick("9"))
# buttonnine.grid(row=1,column=2)

# buttonminus=Button(window,text="-",padx=20,pady=20,command=lambda:handleClick("-"))
# buttonminus.grid(row=1,column=3)

# buttonfour=Button(window,text="4",padx=20,pady=20,command=lambda:handleClick("4"))
# buttonfour.grid(row=2,column=0)

# buttonfive=Button(window,text="5",padx=20,pady=20,command=lambda:handleClick("5"))
# buttonfive.grid(row=2,column=1)

# buttonsix=Button(window,text="6",padx=20,pady=20,command=lambda:handleClick("6"))
# buttonsix.grid(row=2,column=2)

# buttonmultiple=Button(window,text="*",padx=20,pady=20,command=lambda:handleClick("*"))
# buttonmultiple.grid(row=2,column=3)

# buttonone=Button(window,text="1",padx=20,pady=20,command=lambda:handleClick("1"))
# buttonone.grid(row=3,column=0)

# buttontwo=Button(window,text="2",padx=20,pady=20,command=lambda:handleClick("2"))
# buttontwo.grid(row=3,column=1)

# buttonthree=Button(window,text="3",padx=20,pady=20,command=lambda:handleClick("3"))
# buttonthree.grid(row=3,column=2)

# buttondivide=Button(window,text="/",padx=20,pady=20,command=lambda:handleClick("/"))
# buttondivide.grid(row=3,column=3)
 
# buttonzerozero=Button(window,text="00",padx=20,pady=20,command=lambda:handleClick("00"))
# buttonzerozero.grid(row=4,column=0) 

# buttonzero=Button(window,text="0",padx=20,pady=20,command=lambda:handleClick("0"))
# buttonzero.grid(row=4,column=1)


# buttonplus=Button(window,text="+",padx=20,pady=20,command=lambda:handleClick("+"))
# buttonplus.grid(row=4,column=2)


# buttonequals=Button(window,text="=",padx=20,pady=20,command=lambda:result())
# buttonequals.grid(row=4,column=3)



# window.mainloop()
import time
from threading import Thread
class greetinghelo(Thread):
    def run(self):
        for i in range(3):
            print("hello")
            time.sleep(1)
class greetinghai(Thread):
    def run(self):
        for i in range(3):
            print("hai")
            time.sleep(1)
obj_helo=greetinghelo()
obj_hai=greetinghai()
start=time.time()
obj_helo.start()
obj_hai.start()
obj_helo.join()
obj_hai.join()    
print("time taken",time.time()-start)