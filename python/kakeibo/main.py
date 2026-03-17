import tkinter
import ui.registration

root = tkinter.Tk()
root.title("家計簿アプリ")
root.geometry("900x600")
root.configure(bg="#f0f0f0")

expenses = ["日付 : ", "商品 : ", "値段 : "]

def create_registration_card():
    # ヘッダー
    header = tkinter.Frame(root, bg="#2f6fbd", height=120)
    header.pack(fill="x")
    ui.registration.create_header(header)

    # メインエリア
    main = tkinter.Frame(root, bg="#f0f0f0")
    main.pack(fill="both", expand=True, padx=30, pady=20)

    # カード作成
    ui.registration.registration_data(main, expenses)



create_registration_card
root.mainloop()