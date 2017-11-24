from tkinter import *
import tkinter.messagebox

def judge() :
    for x in 0, 3, 6 :
        if list[x]["text"] == list[x+1]["text"] == list[x+2]["text"] != "     " :
            end(list[x]["text"])
        
    for y in range(3) :
        if list[y]["text"] == list[y+3]["text"] == list[y+6]["text"] != "     " :
            end(list[y]["text"])

    if list[0]["text"] == list[4]["text"] == list[8]["text"] != "     " :
        end(list[0]["text"])

    if list[2]["text"] == list[4]["text"] == list[6]["text"] != "     " :
        end(list[2]["text"])

def end(Winner) :

    tkinter.messagebox.showinfo("승리", "Player " + Winner + "가 이겼습니다." +  "\n\n만약 게임을 다시 하고 싶으시다면 다음에 나오는 창에서 ok 를 누른 후 다시 시작해주세요.")
    quit()
    
def checked(i) :
    global player
    button = list[i]

    if button["text"] != "     " :
        return
    button["text"] = player 
    button["bg"] = "yellow"

    if player == "X" :
        player = "O"
        button["bg"] = "yellow"
        judge()
    else :
        player = "X"
        button["bg"] = "lightgreen"
        judge()

window = Tk()
player = "X"
list= []

for i in range(9) :
    b = Button(window, text="     ", command=lambda k=i: checked(k))
    b.grid(row=i//3, column=i%3)
    list.append(b)

window.mainloop()
