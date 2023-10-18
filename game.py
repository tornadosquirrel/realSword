from tkinter import *
whichSword = "나뭇가지"
whichEquipment = "잠옷"
power = "10"
hp = "100"
money = "1000"
upgrade = "0"

ui = Tk() # GUI 생성 
game_window = Toplevel(ui)

def start_game():
  # 기존 UI 숨기기
  ui.withdraw()
    
# 게임 씬 생성
  game_window.title("메뉴")
  game_window.geometry("1920x1080")
  game_window.configure(bg="white")
  game_window.attributes('-fullscreen',True)
  game_window.deiconify()

def show_credit_window():
  # 새로운 창 생성
  credit_window = Toplevel(ui)
  credit_window.title("크레딧")
    
  # 크레딧 내용 표시
  credit_label = Label(credit_window, text="제작\n20606 백재하\n\nSpecial Thanks\n203** 이성민\n201** 남준서\n\n제작기간 : 일")
  credit_label.pack(padx=20, pady=20)

ui.title("타이틀")
ui.geometry("1920x1080")
ui.configure(bg="white")
ui.attributes('-fullscreen',True)

label = Label(ui, text="검강화", anchor="n", font=("Arial", 100), bg="white")
label.pack(pady=300)

button = Button(ui, text="게임 시작", font=("Arial", 50), highlightbackground="black", command=start_game)
button.pack()

credit_button = Button(ui, text="크레딧", font=("Arial", 50), highlightbackground="black", command=show_credit_window)
credit_button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

# 게임 내용 표시

# 함수: 내정보 버튼 클릭 시 실행될 동작
def show_my_info():
  myinfo_window = Toplevel(ui)
  myinfo_window.title("내정보")
    
  # 크레딧 내용 표시
  myinfo = Label(myinfo_window, text=f"현재 검 : {whichSword}(+{upgrade})\n현재 장비 : {whichEquipment}\n공격력 : {power}\n체력 : {hp}\n소지금 : {money}")
  myinfo.pack(padx=20, pady=20)

# 함수: 인벤토리 버튼 클릭 시 실행될 동작
def show_inventory():
  inventory = Toplevel(ui)
  inventory.title("인벤토리")
    
  # 크레딧 내용 표시
  inventory = Label(inventory, text="제작\n20606 백재하\n\nSpecial Thanks\n203** 이성민\n201** 남준서\n\n제작기간 : 일")
  inventory.pack(padx=20, pady=20)

# 함수: 검강화 버튼 클릭 시 실행될 동작
def strengthen_health():
  print("검강화 버튼이 클릭되었습니다.")

# 함수: 상점 버튼 클릭 시 실행될 동작
def open_shop():
  print("상점 버튼이 클릭되었습니다.")

# 함수: 보스잡기 버튼 클릭 시 실행될 동작
def fight_boss():
  print("보스잡기 버튼이 클릭되었습니다.")

# 함수: 타이틀 화면으로 돌아가는 동작
def go_to_title_screen():
  game_window.withdraw()
  ui.deiconify()

title_screen_butten_frame = Frame(game_window) # 프레임 생성

title_screen_butten_frame.pack(pady=(50)) # 프레임을 게임 창에 배치

title_screen_butten_frame.columnconfigure(0, weight=1) # 열의 가중치 설정 (중앙 정렬을 위해 필요)

my_info_button = Button(game_window, text="내정보", font=("Arial", 40), command=show_my_info)
my_info_button.pack(pady=(20))

inventory_button = Button(game_window, text="인벤토리", font=("Arial", 40), command=show_inventory)
inventory_button.pack(pady=(20))

strengthen_health_button = Button(game_window, text="검강화", font=("Arial", 40), command=strengthen_health)
strengthen_health_button.pack(pady=(20))

shop_button = Button(game_window, text="상점", font=("Arial", 40), command=open_shop)
shop_button.pack(pady=(20))

fight_boss_butten = Button(game_window, text="보스잡기", font=("Arial", 40), command=fight_boss)
fight_boss_butten.pack(pady=(20))

title_screen_butten = Button(game_window, text ="타이틀 화면으로", font=('Arial',40), command=lambda :go_to_title_screen())
title_screen_butten.pack(pady=(20))

ui.mainloop()