import random
import tkinter as tk


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.position = 0
        self.name = f"Player {player_id}"

    def move(self, steps):
        for _ in range(steps):
            self.position += 1

        if self.position > 50:
            self.position = 50

    def get_position(self):
        return self.position

player1 = Player(1)
player2 = Player(2)
goaled = False
current_player = player1  # 最初のプレイヤーをplayer1に設定

#print(player1.player_id)
#print(player2.player_id)

def dice():
    return random.randint(1, 6)    
        

#リセットボタンをクリックされたとき
def reset():
    #ボックスの中身を消去
    Box.delete(0, 'end')
    Box_p1.delete(0, 'end')
    Box_p2.delete(0, 'end')
    Box_turn.delete(0, 'end')

    #プレイヤーの位置をリセット
    player1.position = 0
    player2.position = 0
    Box_p1.insert(0, "P1:" + str(player1.get_position()))
    Box_p2.insert(0, "P2:" + str(player2.get_position()))
    Box_turn.insert(0, "Player 1's turn")
    #グローバル変数をリセット
    
    goaled = False
    current_player = player1

#赤いボタンをクリックされたとき    
def buttonClicked():
    global current_player,goaled

    if goaled:
        return  # ゲームが終了している場合は何もしない

    #現在のプレイヤーのボックスを取得   
    if current_player == player1:
        current_box = Box_p1
    else:
        current_box = Box_p2

    current_box.delete(0, 'end')
    Box_turn.delete(0, 'end')
    
    current_box.delete(0, 'end')
    Box.delete(0, 'end')
    result=dice()
    Box.insert(0, result)
    
    current_player.move(result)
    current_box.insert(0, f"P{current_player.player_id}:{current_player.get_position()}")
    if current_player.get_position() >= 50:
            Box_turn.delete(0, 'end')
            Box_turn.insert(0, f"{current_player.name} wins!")
            goaled = True

    #プレイヤーを切り替える       
    if not goaled:
        if current_player == player1:
                current_player = player2
        else:
                current_player = player1
        Box_turn.insert(0, f"{current_player.name}'s turn")

#GUIの作成
root = tk.Tk()
root.title("Two Player Sugoroku Game")
root.geometry("400x300")
root.resizable(True, True)




#さいころの目が表示されるボックス
Box = tk.Entry(width=10, fg="#000000", justify="center", font=("Helvetica", 30))
Box.place(x=150, y=5)

#player1の位置が表示されるボックス
Box_p1 = tk.Entry(width=5, fg="#ff0000", justify="center", font=("Helvetica", 30))
Box_p1.place(x=100, y=65)
Box_p1.insert(0, "P1:" + str(player1.get_position()))

#player2の位置が表示されるボックス
Box_p2 = tk.Entry(width=5, fg="#0000ff", justify="center", font=("Helvetica", 30))
Box_p2.place(x=300, y=65)
Box_p2.insert(0, "P2:" + str(player2.get_position()))

#さいころを振るボタン
button_dice = tk.Button(text='Roll Dice',width = 11, bg='#f9c74f', command=buttonClicked)
button_dice.place(x=170, y=200)

Box_turn = tk.Entry(width=20, fg="#000000", justify="center", font=("Helvetica", 20))
Box_turn.place(x=100, y=150)
Box_turn.insert(0, f"{current_player.name}'s turn")

#リセットボタン
button2 = tk.Button(text='RESET', width=11, bg='#3289a8', command=reset)
button2.place(x=315, y=200)


root.mainloop()
