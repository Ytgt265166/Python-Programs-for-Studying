import random
import tkinter as tk
import tkinter.scrolledtext  # scrolledtextをインポート

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.position = 0
        self.name = f"Player {player_id}"

    def move(self, steps):
        self.position += steps
        if self.position > 20:
            self.position = 20

    def get_position(self):
        return self.position

player1 = Player(1)
player2 = Player(2)

current_player = player1  # 最初のプレイヤーをplayer1に設定

#print(player1.player_id)
#print(player2.player_id)

def dice():
    return random.randint(1,3)    
        

#リセットボタンをクリックされたとき
def reset():
    Box.delete(0, 'end')
    Box_p1.delete(0, 'end')
    Box_p2.delete(0, 'end')

#赤いボタンをクリックされたとき    
def buttonClicked():
    if current_player == player1:
        current_box = Box_p1
    else:
        current_box = Box_p2

    Box_turn.delete(0, 'end')
    Box_turn.insert(0, f"{current_player.name}'s turn")    
    current_box.delete(0, 'end')
    result=dice()
    current_player.move(result)
    current_box.insert(0, current_player.get_position()) 
    if current_player == player1:
            current_player = player2
    else:
            current_player = player1

#GUIの作成
root = tk.Tk()
root.title("Two Player Sugoroku Game")
root.geometry("400x300")
root.resizable(True, True)

Box_turn = tk.Entry(width=20, fg="#000000", justify="center", font=("Helvetica", 30))
Box_turn.place(x=20, y=5)

#さいころの目が表示されるボックス
Box = tk.Entry(width=20, fg="#000000", justify="center", font=("Helvetica", 30))
Box.place(x=20, y=25)

#player1の位置が表示されるボックス
Box_p1 = tk.Entry(width=20, fg="#ff0000", justify="center", font=("Helvetica", 30))
Box_p1.place(x=20, y=45)

#player2の位置が表示されるボックス
Box_p2 = tk.Entry(width=20, fg="#0000ff", justify="center", font=("Helvetica", 30))
Box_p2.place(x=20, y=75)

#赤いボタン
button = tk.Button(text='NEXT NUMBER', width=11, bg='#eb4034', command=buttonClicked)
button.place(x=75, y=80)

#さいころを振るボタン
button_dice = tk.Button(text='Roll Dice',width = 11, bg='#f9c74f', command=dice)
button_dice.place(x=150, y=80)

#リセットボタン
button2 = tk.Button(text='RESET', width=11, bg='#3289a8', command=reset)
button2.place(x=295, y=80)



