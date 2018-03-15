#dic = {}

with open("dict.txt") as f:
    for line in f.readlines():
        key, val = line.split(":")
        dic[strip(key)] = strip(val)

#print(dic)

# 기본 준비 과정..
from tkinter import *
root = Tk()

# 사용가능한 객체들이에요! - Widget 이라고 부르더군요..
lbl = Label(root, text="Keyword", width=10, height=1) # Label - 그날 텍스트 있는 라벨이다.
txt = Entry(root) # Entry - 솔직히 TextBox..
btn = Button(root, text="Ok") # Button - 말 그대로 버튼이다.
cbt = Checkbutton(root) # CheckBox
lbx = Listbox(root,) # ListBox
# Radiobutton - 옵션 버튼
# Message - Label과 비슷하지만 자동래핑이 가능하다
# Scale - 슬라이스바
# Scrollbar - 스크롤바
# Text - 멀티라인 텍스트 박스로서 일부 Rich Text기능 제공
# Menu - 말그대로 Menu Pane
# Menubutton - 메뉴버튼
# Toplevel - 추가적인 윈도우, 다이얼로그를 만들 경우 사용합니다.
# Frame - 컨테이너, 다른 위젯들을 그룹화 할 때 사용한다.
# Canvas - 그래프와 점들로 그림을 그릴 수 있다, 커스템 위젯을 만드는데 사용

# 화면상에 배치하기 (method)
# pack(side, fill, padx, pady, expand) - 화면에 빈틈없이 하고자 합니다.
# place() - 절대좌표를 지정한다!
# grid(row, column) - 테이블레이아웃에 배치한다..!
# 구체적인 값들은 인터넷 Reference를 찾아가며 해야할듯 하다.
lbl.pack(fill=X, side=LEFT, padx=10)
txt.pack()
btn.pack()
cbt.pack()
lbx.pack()

# Frame Widget 수정하기
root.title("타이트을")
root.geometry('500x400') # 가로 세로 가로offset 세로offset

root.mainloop()