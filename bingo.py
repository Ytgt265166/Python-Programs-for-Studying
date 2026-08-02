import random
import tkinter as tk
import tkinter.scrolledtext  # scrolledtextをインポート

hai = []

#無作為に整数を出力
def randomn():
    r = random.randint(1, 75)
    while r in hai:
        r=random.randint(1,75)
    hai.append(r)
    return r
    
    
        
#配列の要素を見せる
def show():
    return hai

#配列の長さを出力
def length():
    return len(hai),"/75 "

#リセットボタンをクリックされたとき
def reset():
    hai.clear()
    Box.delete(0, 'end')
    Box2.delete('1.0', 'end') 
    Box3.delete(0,'end')

#赤いボタンをクリックされたとき    
def buttonClicked():
    Box.delete(0, 'end')
    Box2.delete('1.0', 'end')  # Box2の内容をすべて削除
    Box3.delete(0,'end')
    result=randomn()
    Box.insert(0, result) 
    Box2.insert('1.0', show())  # Box2の内容を更新
    Box3.insert(0,length())

#GUIの作成
root = tk.Tk()
root.title("Bingo Machine")
root.geometry("400x300")
root.resizable(True, True)

#新しい数字が出力されるボックス
Box = tk.Entry(width=20, fg="red", justify="center", font=("Helvetica", 30))
Box.place(x=20, y=25)

#赤いボタン
button = tk.Button(text='NEXT NUMBER', width=11, bg='#eb4034', command=buttonClicked)
button.place(x=75, y=80)

#リセットボタン
button2 = tk.Button(text='RESET', width=11, bg='#3289a8', command=reset)
button2.place(x=295, y=80)

#配列を出力するボックス
Box2 = tkinter.scrolledtext.ScrolledText(
    root, 
    width=40, 
    font=("Helvetica", 15)
)
Box2.place(x=20, y=115)

#長さを出力するボックス
Box3 = tk.Entry(width=10,justify="center", font=("Helvetica", 15))
Box3.place(x=170, y=80)
root.mainloop()
