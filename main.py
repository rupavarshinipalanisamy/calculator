import tkinter 

#creating the main window
root = tkinter.Tk()
root.minsize(280, 500)
root.title('calculator')

result = tkinter.StringVar()
result.set(0)  
result2 = tkinter.StringVar()  
result2.set('')

label = tkinter.Label(root, font=('Courier', 20), bg='#EEE9E9', bd='9', fg='#828282', anchor='se', textvariable=result2)
label.place(width=280, height=170)
label2 = tkinter.Label(root, font=('courier', 30), bg='#EEE9E9', bd='9', fg='black', anchor='se', textvariable=result)
label2.place(y=170, width=280, height=60)


#Adding the number buttons
btn7 = tkinter.Button(root, text='7', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('7'))
btn7.place(x=0, y=285, width=70, height=55)
btn8 = tkinter.Button(root, text='8', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('8'))
btn8.place(x=70, y=285, width=70, height=55)
btn9 = tkinter.Button(root, text='9', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('9'))
btn9.place(x=140, y=285, width=70, height=55)

btn4 = tkinter.Button(root, text='4', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('4'))
btn4.place(x=0, y=340, width=70, height=55)
btn5 = tkinter.Button(root, text='5', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('5'))
btn5.place(x=70, y=340, width=70, height=55)
btn6 = tkinter.Button(root, text='6', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('6'))
btn6.place(x=140, y=340, width=70, height=55)

btn1 = tkinter.Button(root, text='1', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('1'))
btn1.place(x=0, y=395, width=70, height=55)
btn2 = tkinter.Button(root, text='2', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('2'))
btn2.place(x=70, y=395, width=70, height=55)
btn3 = tkinter.Button(root, text='3', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('3'))
btn3.place(x=140, y=395, width=70, height=55)
btn0 = tkinter.Button(root, text='0', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('0'))
btn0.place(x=70, y=450, width=70, height=55)

#Adding Operation Buttons
btnac = tkinter.Button(root, text='AC', bd=0.5, font=('courier', 20), fg='orange', command=lambda: pressCompute('AC'))
btnac.place(x=0, y=230, width=70, height=55)
btnback = tkinter.Button(root, text='←', font=('courier', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressCompute('b'))
btnback.place(x=70, y=230, width=70, height=55)
btndivi = tkinter.Button(root, text='÷', font=('courier', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressCompute('/'))
btndivi.place(x=140, y=230, width=70, height=55)
btnmul = tkinter.Button(root, text='×', font=('courier', 20), fg="#4F4F4F", bd=0.5, command=lambda: pressCompute('*'))
btnmul.place(x=210, y=230, width=70, height=55)
btnsub = tkinter.Button(root, text='-', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressCompute('-'))
btnsub.place(x=210, y=285, width=70, height=55)
btnadd = tkinter.Button(root, text='+', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressCompute('+'))
btnadd.place(x=210, y=340, width=70, height=55)
btnequ = tkinter.Button(root, text='=', bg='orange', font=('courier', 20), fg=('#4F4F4F'), bd=0.5,
                        command=lambda: pressEqual())
btnequ.place(x=210, y=395, width=70, height=110)
btnper = tkinter.Button(root, text='%', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressCompute('%'))
btnper.place(x=0, y=450, width=70, height=55)
btnpoint = tkinter.Button(root, text='.', font=('courier', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressCompute('.'))
btnpoint.place(x=140, y=450, width=70, height=55)

#Global list andBoolean Variables
lists = []  
isPressSign = False 
isPressNum = False

#When a Number is Pressed
def pressNum(num): 
    global lists 
    global isPressSign
    if isPressSign == False:
        pass
    else:  
        result.set(0)
        isPressSign = False

    oldnum = result.get()  
    if oldnum == '0':  
        result.set(num)
    else:  
        newnum = oldnum + num
        result.set(newnum)  

#When Equalto is Pressed
def pressCompute(sign):
    global lists
    global isPressSign
    num = result.get()  
    lists.append(num)  

    lists.append(sign)  
    isPressSign = True

    if sign == 'AC':  
        lists.clear()
        result.set(0)
    if sign == 'b':  
        a = num[0:-1]
        lists.clear()
        result.set(a)


def pressEqual():
    global lists
    global isPressSign

    curnum = result.get()  
    lists.append(curnum)

    computrStr = ''.join(lists)  

    try:
        content = result.get();
        endNum = eval(computrStr)  
        result.set(content + '\n' + str(result))
    except:
        result.set('error')



    #  a = str(endNum)
    #  b = '='+a            
    #  c = b[0:10]           
    result.set(endNum)  
    result2.set(computrStr)  
    lists.clear()  


root.mainloop()
