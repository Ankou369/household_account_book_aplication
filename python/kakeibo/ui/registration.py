import tkinter
import datetime
import db.expense

def registration_data(parent, expenses):
    card = tkinter.Frame(parent, bg = "#e5e5e5", bd = 0)
    card.pack(fill = "x", pady = 15)

    title_label = tkinter.Label(
        card,
        text = "データの登録",
        font = ("Noto Sans JP", 16, "bold"),
    )
    title_label.pack(anchor="center", padx = 20, pady = 10)

    def validate_date(date_str):
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return None
        

    entries = {}
    for expense in expenses:
        row = tkinter.Frame(card, bg = "#e5e5e5")
        row.pack(fill = "x", padx = 30, pady = 5)

        label = tkinter.Label(
            row,
            text = expense,
            font = ("Meiryo", 11),
            bg = "#e5e5e5",
            width = 8,  # 横幅を揃える
            padx = 10,
            anchor = "w"
        )
        label.pack(side = "left")

        #右側のスペース
        label = tkinter.Label(
            row,
            bg = "#e5e5e5",
            width = 3,
            anchor = "e"
        )
        label.pack(side = "right")

        entry = tkinter.Entry(row, font = ("Meiryo", 11))
        entry.pack(side = "left", fill = "x", expand = True)

        
        entries[expense] = entry

    def on_click():
        date_str = entries["日付 : "].get()
        item = entries["商品 : "].get()
        price = int(entries["値段 : "].get())
        date = validate_date(date_str)

        db.expense.add_expense(date, item, price)

    button = tkinter.Button(
            card, 
            text = "登録",
            font = ("Times New Roman", 24),
            command = on_click
            )

    button.pack(anchor="center", padx = 20, pady = 10)