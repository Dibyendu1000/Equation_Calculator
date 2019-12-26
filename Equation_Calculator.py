import tkinter

root=tkinter.Tk()
root.iconbitmap('image1.ico')

def sridhar():
    a=float(exp_field1.get())
    b=float(exp_field2.get())
    c=float(exp_field3.get())
    D=b**2-4*a*c
    if(D==0):
        Result['text']=round(-b/(2*a),4)
    elif(D<0):
        D=(abs(D))**0.5
        res1=str(round(-b/(2*a),4))+" + "+str(round(D/(2*a),4))+" i"
        res2="\n"+str(round(-b/(2*a),4))+" - "+str(round(D/(2*a),4))+" i"
        Result['text']=res1+","+res2
    else:
        D=D**0.5
        res1=round((-b+D)/(2*a),4)
        res2=round((-b-D)/(2*a),4)
        Result['text']=str(res1)+" , "+str(res2)
    
root.title("Quadratic Roots Calculator")
root.geometry("360x275")

equation1 = tkinter.StringVar() 
exp_field1 = tkinter.Entry(root, textvariable=equation1, width=4, font="5")
exp_field1.place(x=10,y=10)
exp_field1.configure(font=("Calibri",17))

equation2 = tkinter.StringVar() 
exp_field2 = tkinter.Entry(root, textvariable=equation2, width=4, font="5")
exp_field2.place(x=110,y=10)
exp_field2.configure(font=("Calibri",17))

equation3 = tkinter.StringVar() 
exp_field3 = tkinter.Entry(root, textvariable=equation3, width=4, font="5")
exp_field3.place(x=210,y=10)
exp_field3.configure(font=("Calibri",17))

x2=tkinter.Label(root, text='x\u00b2   +', font="5")
x2.place(x=60,y=10)
x2.configure(font=("Calibri",17))

x=tkinter.Label(root, text='x   +', font="5")
x.place(x=160,y=10)
x.configure(font=("Calibri",17))

eq=tkinter.Label(root, text='  =    0', font="5")
eq.place(x=260,y=10)
eq.configure(font=("Calibri",17))

cal=tkinter.Button(root, text='Roots are:', command=sridhar, height=2, width=10,font='5',bg='orange')
cal.place(x=110,y=60)


Display=tkinter.Label(root,text="x =",font='5')
Display.place(x=75,y=130)
Display.configure(font=("Calibri",17))

Result=tkinter.Label(root,text=None,font='5')
Result.place(x=110,y=130)
Result.configure(font=("Calibri",17))


root.mainloop()
