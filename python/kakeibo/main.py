import tkinter
import ui.registration,ui.header,ui.show_data


root = tkinter.Tk()
root.title("家計簿アプリ")
root.geometry("900x800")
root.configure(bg="#f0f0f0")

expenses = ["日付 : ", "商品 : ", "値段 : "]
def create_header():
    # ヘッダー
    header = tkinter.Frame(root, bg="#2f6fbd", height=120)
    header.pack(fill = "x")
    ui.header.create_header(header)

def create_registration_card():
    regi_card = tkinter.Frame(root, bg="#f0f0f0")
    regi_card.pack(fill="both", padx=30, pady=(10,0))

    # カード作成
    ui.registration.registration_data(regi_card, expenses)

def create_show_data_card():
    show_card = tkinter.Frame(root, bg="#f0f0f0")
    show_card.pack(fill="both", padx=30, pady=(10,0))

    # カード作成
    ui.show_data.show_data(show_card, expenses)




create_header()
create_registration_card()
create_show_data_card()
root.mainloop()