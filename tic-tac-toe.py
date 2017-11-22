from tkinter import *

'''
Player class
'''
class Player:
    # 플레이어는 특정 마크를 가지고, 해당 마크를 선택한 버튼에 표시
    def __init__(self, mark):
        self.mark = mark
        self.occupied = [] # 플레이어가 현재까지 선택한 버튼의 행렬값을 저장할 리스트

    # 플레이어가 특정 버튼을 선택하면 해당 버튼의 행렬값을 리스트에 추가
    def occupy(self, buttonIdx):
        self.occupied.append((buttonIdx // 3, buttonIdx % 3))

    # 플레이어가 특정 버튼을 선택한 적이 있는지 확인
    def isOccupying(self, buttonIdx):
        if (buttonIdx // 3, buttonIdx % 3) in self.occupied:
            return True
        else:
            return False

    # 보드판의 행 혹은 열을 모두 소유하고 있는지 확인 (0: 행 / 1: 열)
    def checkRowCol(self, which):
        winChecker = [ 0, 0, 0 ]

        for t in self.occupied: # 소유하고 있는 행 혹은 열의 갯수 증가
            winChecker[t[which]] += 1

        for i in winChecker:
            if i >= 3:
                return True

        return False

    # 보드판의 해당 대각선을 모두 소유하고 있는지 확인
    def checkDiagonal(self, condition):
        return condition[0] in self.occupied and condition[1] in self.occupied and condition[2] in self.occupied

    # 플레이어가 게임에서 승리할 수 있는지 확인
    def canWin(self): # 행 / 열 / 대각선 중 하나라도 모두 소유하고 있으면 승리 가능
        return self.checkRowCol(0) or self.checkRowCol(1) or self.checkDiagonal([ (0, 0), (1, 1), (2, 2) ]) or self.checkDiagonal([ (0, 2), (1, 1), (2, 0) ])
'''
end of Player class
'''

'''
checked method
'''
def checked(i):
    for player in players: # 모든 플레이어 중 한 명이라도 선택된 버튼을 소유하고 있으면 현재 플레이어는 해당 버튼 소유 불가
        if player.isOccupying(i):
            return

    # 현재 턴의 플레이어 설정
    global turn
    button = list[i]
    curPlayer = players[turn % 2]

    # 선택된 버튼에 현재 플레이어의 마크를 표시하고 현재 플레이어가 해당 버튼을 소유
    button["text"] = curPlayer.mark
    curPlayer.occupy(i)

    # 현재 플레이어에 따라 버튼 색을 다르게 지정
    if curPlayer.mark == "X":
        button["bg"] = "yellow"
    else:
        button["bg"] = "lightgreen"

    # 현재 플레이어가 이길 수 있는지 확인
    if curPlayer.canWin():
        winnerIs(curPlayer) # 가능하면 현재 플레이어가 승리
    else:
        turn += 1 # 불가능하면 턴 변경

        if turn > 8: # 모든 버튼이 선택됐음에도 승부가 나지 않으면 무승무 문구 표시
            drawMsg = Message(window, text="Draw")
            drawMsg.grid(row=4, column=1)
'''
end of checked method
'''

'''
winnerIs method
'''
def winnerIs(player):
    # 승리한 플레이어를 전달받아 해당 플레이어가 승리했음을 문구로 표시
    winnerMsg = Message(window, text="Player " + player.mark + " wins.")
    winnerMsg.grid(row=4, column=1)

    for b in list: # 게임이 종료됐으므로 각 버튼의 명령 제거
        b["command"] = ""
'''
end of winnerIs method
'''

'''
main
'''
window = Tk()
players = [ Player("X"), Player("O") ] # 2명의 플레이어
list = [] # 버튼의 리스트

# 9개의 버튼을 생성하고 버튼에 checked method를 호출할 수 있도록 설정한 뒤 위치를 지정하고 해당 버튼을 리스트에 추가
for i in range(9):
    b = Button(window, text="     ", command=lambda k=i: checked(k))
    b.grid(row=i//3, column=i%3)
    list.append(b)

# 첫 턴은 플레이어 0부터 시작
turn = 0
window.mainloop()
'''
end of main
'''
