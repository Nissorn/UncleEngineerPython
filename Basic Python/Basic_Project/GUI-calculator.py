#GUI-claculator.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('Program USD to BATH')
GUI.geometry('700x600')

bg = PhotoImage(file='dollarlogo.png')

#Picture
BG = Label(GUI, image=bg )
BG.pack()

#Title Text
L = Label(GUI,text='Enter USD', font=(None,20))
L.pack()

#Input 
usdInput = StringVar() #ตัวแปรใช้เก็บข้อความเมื่อพิมพ์เสร็จ
E1 = ttk.Entry(GUI, textvariable=usdInput, font=(None,20))
E1.pack()

def Cal():
	try:
		usd = float(usdInput.get()) 
		calc = usd * 34.22 #คำนวณ
		messagebox.showinfo('Tranfer USD to BATH',f'{usd} USD = {calc} Bath') #ใช้f string แสดงผล
		E1.focus() #ทำให้curserไปอยู่ที่input
	except:
		messagebox.showwarning('Error','Please Enter Number') #แสดงerror
		usdInput.set('') #ตั้งให้ช่องนี้ว่าง
		E1.focus() #ทำให้curserไปอยู่ที่input

#Button
B = ttk.Button(GUI, text='calculate', command=Cal)
B.pack(ipadx=30, ipady=20)



GUI.mainloop() #ให้Program Runไว้ตลอดเวลา