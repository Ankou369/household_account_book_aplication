import tkinter
import datetime
from dataclasses import dataclass

root = tkinter.Tk()
root.title("家計簿アプリ")
root.geometry("900x600")
root.configure(bg="#f0f0f0")

expenses = ["date", "item", "price"]

# ヘッダー
header = tkinter.Frame(root, bg="#2f6fbd", height=120)
header.pack(fill="x")

title = tkinter.Label(header,
                      text="家計簿アプリ",
                      font=("Noto Sans JP", 24, "bold"),
                      bg="#2f6fbd",
                      fg="white")
title.pack(pady=(30,5))

subtitle = tkinter.Label(header,
                    text="支出管理ページ",
                    font=("Noto Sans JP", 12),
                    bg="#2f6fbd",
                    fg="white")
subtitle.pack()


# メインエリア
main = tkinter.Frame(root, bg="#f0f0f0")
main.pack(fill="both", expand=True, padx=30, pady=20)

def registration_data(parent, expenses):
    card = tkinter.Frame(parent, bg = "#e5e5e5", bd = 0)
    card.pack(fill = "x", pady = 15)

    title_label = tkinter.Label(
        card,
        text = "データの登録",
        font = ("Noto Sans JP", 16, "bold"),
    )
    title_label.pack(anchor="center", padx = 20, pady = 10)

    for expense in expenses:
        label = tkinter.Label(
            card,
            text = expense,
            font = ("Meiryo", 11),
            bg = "#e5e5e5"
        )
    label.pack(anchor = "w", padx = 40)

    button = tkinter.Button(
            card, 
            text = "登録",
            font = ("Times New Roman", 24))

    button.pack(anchor="center", padx = 20, pady = 10)



# カード作成
registration_data(main, expenses)




root.mainloop()