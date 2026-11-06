import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import winsound
import ast
import math

root=ThemedTk(theme="equilux")

root.geometry("500x600")
root.title("Calculator")
root.resizable(False,False)
style=ttk.Style(root)
style.configure("TButton",
    font=("Aral",18,"bold"))
style.configure(
    "TEntry",
    font=("Arial",28),
    padding=12
)

display=ttk.Entry(root,justify="right",font=("Arial",28))
for i in range(4):
    root.grid_columnconfigure(i,weight=1)
for i in range(7):
    root.grid_rowconfigure(i,weight=1)
display.grid(row=0,column=0,rowspan=2,columnspan=4,sticky="nsew")


def play_sound(filename):
   winsound.PlaySound(filename,winsound.SND_FILENAME | winsound.SND_ASYNC)
def number_click(char):
    play_sound("sounds/number.wav")
    insert_char(char)
def operator_click(char):
    play_sound("sounds/number.wav")
    insert_char(char)
def cross_click():
    play_sound("sounds/cross.wav")
    cut_last_char()
def empty_click():
    play_sound("sounds/empty.wav")
    clear_display()
def equal_click():
    play_sound("sounds/equal.wav")
    calculate()

button_AC=tk.Button(root,text="AC",bg="#D94B70",fg="white",activebackground="#F06A89",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_bracket=tk.Button(root,text="( )",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_modulo=tk.Button(root,text="%",bg="#245B78",fg="white",activebackground="#347FA3",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_devide=tk.Button(root,text="÷",bg="#245B78",fg="white",activebackground="#347FA3",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_multiply=tk.Button(root,text="×",bg="#245B78",fg="white",activebackground="#347FA3",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_minus=tk.Button(root,text="-",bg="#245B78",fg="white",activebackground="#347FA3",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_plus=tk.Button(root,text="+",bg="#245B78",fg="white",activebackground="#347FA3",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_cross=tk.Button(root,text="⌫",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_equal=tk.Button(root,text="=",bg="#7655E8",fg="white",activebackground="#967AF5",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_decimal=tk.Button(root,text=".",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_1=tk.Button(root,text="1",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_2=tk.Button(root,text="2",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_3=tk.Button(root,text="3",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_4=tk.Button(root,text="4",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_5=tk.Button(root,text="5",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_6=tk.Button(root,text="6",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_7=tk.Button(root,text="7",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_8=tk.Button(root,text="8",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_9=tk.Button(root,text="9",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
button_0=tk.Button(root,text="0",bg="#293550",fg="white",activebackground="#3B4D70",activeforeground="white",font=("Arial", 18, "bold"),relief="flat",bd=0)
#button layout
button_AC.grid(row=2,column=0,sticky="nsew")
button_bracket.grid(row=2,column=1,sticky="nsew")
button_modulo.grid(row=2,column=2,sticky="nsew")
button_devide.grid(row=2,column=3,sticky="nsew")
button_7.grid(row=3,column=0,sticky="nsew")
button_8.grid(row=3,column=1,sticky="nsew")
button_9.grid(row=3,column=2,sticky="nsew")
button_multiply.grid(row=3,column=3,sticky="nsew")
button_4.grid(row=4,column=0,sticky="nsew")
button_5.grid(row=4,column=1,sticky="nsew")
button_6.grid(row=4,column=2,sticky="nsew")
button_minus.grid(row=4,column=3,sticky="nsew")
button_1.grid(row=5,column=0,sticky="nsew")
button_2.grid(row=5,column=1,sticky="nsew")
button_3.grid(row=5,column=2,sticky="nsew")
button_plus.grid(row=5,column=3,sticky="nsew")
button_0.grid(row=6,column=0,sticky="nsew")
button_decimal.grid(row=6,column=1,sticky="nsew")
button_cross.grid(row=6,column=2,sticky="nsew")
button_equal.grid(row=6,column=3,sticky="nsew")

def clear_display():
    display.delete(0,tk.END)
button_AC.config(command=empty_click)

def cut_last_char():
    cursor_position=display.index(tk.INSERT)
    if cursor_position>0:
        display.delete(cursor_position-1,cursor_position)
button_cross.config(command=cross_click)

result_displayed=False
def insert_char(char):
    global result_displayed
    if result_displayed:
        if char.isdigit():
            clear_display()
    result_displayed=False
    check_display()
    content=display.get()
    if char=="()":
        if not content:
            char="("
        else:
            last_char=content.rstrip()[-1]
            opening=content.count("(")
            closing=content.count(")")
            if last_char.isdigit() and opening>closing:
                char=")"
            elif last_char in "+-%÷×":
                char="("
            elif last_char.isdigit() and opening==closing:
                char="×("
            elif last_char==")" and opening==closing:
                char="×("
            elif last_char==")" and opening>closing:
                char=")"
            elif last_char=="(":
                char="("
    elif char.isdigit():
        if content:
            last_char=content.strip()[-1]
            if last_char==")":
                char=f"×{char}"
    display.insert(tk.END,char)
def check_display():
    content=display.get()
    if content in ["Cannot devide by zero","Unsopported Expression","Invalid expression"]:
        clear_display()

button_0.config(command=lambda:number_click("0"))
button_1.config(command=lambda:number_click("1"))
button_2.config(command=lambda:number_click("2"))
button_3.config(command=lambda:number_click("3"))
button_4.config(command=lambda:number_click("4"))
button_5.config(command=lambda:number_click("5"))
button_6.config(command=lambda:number_click("6"))
button_7.config(command=lambda:number_click("7"))
button_8.config(command=lambda:number_click("8"))
button_9.config(command=lambda:number_click("9"))
button_decimal.config(command=lambda:number_click("."))
button_multiply.config(command=lambda:operator_click(" × "))
button_plus.config(command=lambda:operator_click(" + "))
button_minus.config(command=lambda:operator_click(" - "))
button_devide.config(command=lambda:operator_click(" ÷ "))
button_modulo.config(command=lambda:operator_click(" % "))
button_bracket.config(command=lambda:operator_click("()"))
def evaluate(node):
    if isinstance(node,ast.Constant):
        if type(node.value) in (int,float):
            return node.value
        raise ValueError("Unsupported value")
    elif isinstance(node,ast.BinOp):
        left=evaluate(node.left)
        right=evaluate(node.right)
        if isinstance(node.op,ast.Add):
            return left + right
        elif isinstance(node.op,ast.Sub):
            return left - right
        elif isinstance(node.op,ast.Mult):
            return left * right
        elif isinstance(node.op,ast.Div):
            try:
                return left / right
            except ZeroDivisionError:
                raise ZeroDivisionError("Cannot devide by zero")
        elif isinstance(node.op,ast.Mod):
            try:
                return left % right
            except ZeroDivisionError:
                raise ZeroDivisionError("Cannot devide by zero")
        elif isinstance(node.op,ast.Pow):
            if left==0:
                if right>0:
                    return 0
                elif right==0:
                    return 1
                elif right<0:
                    raise ZeroDivisionError("Zero cannot be raised to a negative power")
            if right==0:
                return 1
            elif right>0:
                if right%1==0:
                    digit_count=math.floor(abs(right)*math.log10(abs(left)))+1
                    if digit_count>100:
                        raise ValueError("Result exceeds 100 digits")
                    return left ** right
                else:
                    if left<0:
                        raise ValueError("Complex numbers are not supported")
                    return left ** right
            elif right<0:
                if left<0:
                    raise ValueError("Complex numbers are not supported")
                return left ** right
        raise ValueError("Unsupported expression")
    elif isinstance(node,ast.UnaryOp):
        operand=evaluate(node.operand)
        if isinstance(node.op,ast.USub):
            return -operand
        elif isinstance(node.op,ast.UAdd):
            return +operand
    raise ValueError("Unsupported expression")
def calculate():
    global result_displayed
    expression=display.get()
    if not expression:
        return
    if "÷" in expression:
        expression=expression.replace("÷","/")
    if "×" in expression:
        expression=expression.replace("×","*")
    try:
        tree=ast.parse(expression,mode="eval")
        calculated_exp=evaluate(tree.body)
    except ValueError as v:
        clear_display()
        display.insert(tk.END,str(v))
    except ZeroDivisionError as z:
        clear_display()
        display.insert(tk.END,str(z))
    except SyntaxError:
        clear_display()
        display.insert(tk.END,"Invalid expression")
    else:
        clear_display()
        display.insert(tk.END,calculated_exp)
        result_displayed=True
button_equal.config(command=equal_click)
root.mainloop()